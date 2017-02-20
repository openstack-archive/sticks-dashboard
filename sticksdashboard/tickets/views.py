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

from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables
from horizon import tabs
from sticksdashboard.api import sticks as sticks_api
from sticksdashboard.tickets import tables as p_tables
from sticksdashboard.tickets import tabs as p_tabs


class IndexView(tables.DataTableView):
    table_class = p_tables.TicketsTable
    template_name = 'tickets/index.html'

    def get_data(self):
        try:
            tickets = sticks_api.ticket_list(self.request)
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve tickets details.'),
                              redirect=self.get_redirect_url())
        return tickets


class DetailView(tabs.TabView):
    tab_group_class = p_tabs.TicketDetailTabs
    template_name = 'tickets/detail.html'
    redirect_url = 'tickets:index'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        ticket = self.get_data()
        context["ticket"] = ticket
        return context

    def get_data(self):
        try:
            return sticks_api.ticket_get(self.request,
                                         self.kwargs['ticket_id'])
        except Exception:
            exceptions.handle(self.request,
                              _('Unable to retrieve ticket details.'),
                              redirect=self.get_redirect_url())

    @staticmethod
    def get_redirect_url():
        return reverse_lazy('horizon:helpdesk:tickets:index')

    def get_tabs(self, request, *args, **kwargs):
        ticket = self.get_data()
        return self.tab_group_class(request, ticket=ticket, **kwargs)
