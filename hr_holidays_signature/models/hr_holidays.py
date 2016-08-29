# -*- coding: utf-8 -*-
# © 2016 ONESTEiN BV (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class HrHolidays(models.Model):
    _inherit = 'hr.holidays'
    
    manager_signature = fields.Binary('Signature manager')
