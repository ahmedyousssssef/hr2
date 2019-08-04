# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class WelcomeCardConverttoleadMass(models.TransientModel):
    _name = "welcome.card.converttolead.mass"
    _description = "Wizard - Welcome Card Convert To Lead"

    @api.multi
    def convert_welcome_card_to_lead(self):
        self.ensure_one()
        active_ids = self._context.get('active_ids')
        orders = self.env['crm.lead'].browse(active_ids)
        for order in orders:
            # if order.state in ['draft', 'sent']:
            #     order.action_confirm()
            print("Order : " , order )