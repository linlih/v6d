/** Copyright 2020-2021 Alibaba Group Holding Limited.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

#ifndef MODULES_BASIC_STREAM_PARALLEL_STREAM_H_
#define MODULES_BASIC_STREAM_PARALLEL_STREAM_H_

#include <memory>
#include <string>
#include <vector>

#include "basic/stream/parallel_stream.vineyard.h"
#include "client/client.h"

namespace vineyard {

/**
 * @brief ParallelStreamBuilder is desinged for building parallel stremas
 *
 */
class ParallelStreamBuilder : public ParallelStreamBaseBuilder {
 public:
  void AddStream(const ObjectID stream_id);

  Status Build(Client& client) override;

 private:
  std::vector<ObjectID> streams_;
};

}  // namespace vineyard

#endif  // MODULES_BASIC_STREAM_PARALLEL_STREAM_H_
