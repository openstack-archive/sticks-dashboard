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

from django.utils.translation import ugettext_lazy as _
from horizon import tables


class TicketsTable(tables.DataTable):
    uuid = tables.Column("id",
                         link=("horizon:helpdesk:tickets:details"),
                         verbose_name="id",)
    name = tables.Column("title", verbose_name=_("Title"))
    version = tables.Column("status", verbose_name=_("Status"))
    provider = tables.Column("start_date", verbose_name=_("Start date"))
    type = tables.Column("project", verbose_name=_("Project"))

    def get_object_id(self, datum):
        return datum.id

    class Meta(object):
        name = "tickets"
        verbose_name = _("Tickets")
