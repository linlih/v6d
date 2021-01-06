#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Alibaba Group Holding Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import numpy as np
import pandas as pd
from pandas.core.internals.blocks import Block
from pandas.core.internals.managers import SingleBlockManager

from vineyard._C import ObjectMeta


def pandas_series_builder(client, value, builder, **kw):
    meta = ObjectMeta()
    meta['typename'] = 'vineyard::Series'
    meta['name'] = json.dumps(value.name)
    meta.add_member('index_', builder.run(client, value.index))
    meta.add_member('value_', builder.run(client, value.to_numpy(), **kw))
    return client.create_metadata(meta)


def pandas_series_resolver(obj, resolver):
    meta = obj.meta
    name = json.loads(meta['name'])
    index = resolver.run(obj.member('index_'))
    np_value = resolver.run(obj.member('value_'))
    block = Block(np_value, slice(0, len(np_value), 1), ndim=1)
    return pd.Series(SingleBlockManager(block, index), name=name)


def register_series_types(builder_ctx, resolver_ctx):
    if builder_ctx is not None:
        builder_ctx.register(pd.Series, pandas_series_builder)

    if resolver_ctx is not None:
        resolver_ctx.register('vineyard::Series', pandas_series_resolver)