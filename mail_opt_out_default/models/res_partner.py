# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _compute_opt_out_default(self):
        company = self.env.user.company_id
        if company.default_opt_out:
            return True
        return False

    _defaults = {
        'opt_out': _compute_opt_out_default,
    }
