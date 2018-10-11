# -*- coding:utf-8 -*-
# Copyright 2018 Huawei Technologies Co.,Ltd.
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License.  You may obtain a copy of the
# License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.

from openstack import proxy2
from openstack.bms.v1 import server as _server

class Proxy(proxy2.BaseProxy):
    def create_server(self, **data):
        """
        post method to create bms server
        :param data: data to create bms server see more info from support website
        :return: :class:`~openstack.bms.v1.server.Servers`
        """
        return self._create(_server.Servers, **data)
