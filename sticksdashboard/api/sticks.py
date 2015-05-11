#
#   Copyright (c) 2015 EUROGICIEL
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

import logging

from openstack_dashboard.api import base
from sticksclient import client as sticks_client

from sticksdashboard.utils import importutils

keystone = importutils.import_any('openstack_dashboard.api.keystone',
                                  'horizon.api.keystone')

LOG = logging.getLogger(__name__)


# @memoized
def sticksclient(request):
    """Initialization of Sticks client."""
    sticks_endpoint = base.url_for(request, 'helpdesk')
    return sticks_client.Client('1',
                                sticks_endpoint,
                                tenant_id=request.user.tenant_id,
                                token=request.user.token.id)


def ticket_list(request):
    """List plugins."""
    return sticksclient(request).tickets.list(
        data={'project': request.user.tenant_id})


def ticket_get(request, ticket_id):
    """Get plugin information."""
    return sticksclient(request).tickets.get(ticket_id)


def ticket_create(request, name='unknown', type='unique',
                  period=None):
    """Create a ticket."""
    return sticksclient(request).tickets.create()
