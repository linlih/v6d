# Copyright 2020-2021 Alibaba Group Holding Limited.
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

# build cpprestsdk
set(WERROR OFF CACHE BOOL "Treat warnings as errors")
set(BUILD_TESTS OFF CACHE BOOL "Build tests.")
set(BUILD_SAMPLES OFF CACHE BOOL "Build sample applications.")
set(CPPREST_EXCLUDE_WEBSOCKETS ON CACHE BOOL "Exclude websockets functionality..")
add_subdirectory(thirdparty/cpprestsdk)
set(CPPREST_INCLUDE_DIR thirdparty/cpprestsdk/Release/include)
set(CPPREST_LIB cpprest)

# build etcd-cpp-apiv3
add_subdirectory(thirdparty/etcd-cpp-apiv3)
set(ETCD_CPP_LIBRARIES etcd-cpp-api)
set(ETCD_CPP_INCLUDE_DIR thirdparty/etcd-cpp-apiv3
                         ${PROJECT_BINARY_DIR}/thirdparty/etcd-cpp-apiv3/proto/gen
                         ${PROJECT_BINARY_DIR}/thirdparty/etcd-cpp-apiv3/proto/gen/proto)
