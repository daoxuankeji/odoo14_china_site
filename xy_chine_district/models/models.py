# -*- coding: utf-8 -*-

from odoo import models, fields, api


class chine_district(models.Model):

    _inherit = 'res.partner'


#     _name = 'xy_chine_district.xy_chine_district'
#     _description = 'xy_chine_district.xy_chine_district'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
