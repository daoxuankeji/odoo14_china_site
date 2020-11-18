# -*- coding: utf-8 -*-
from odoo import http


# class XyChineDistrict(http.Controller):
#     @http.route('/xy_chine_district/xy_chine_district/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xy_chine_district/xy_chine_district/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xy_chine_district.listing', {
#             'root': '/xy_chine_district/xy_chine_district',
#             'objects': http.request.env['xy_chine_district.xy_chine_district'].search([]),
#         })

#     @http.route('/xy_chine_district/xy_chine_district/objects/<model("xy_chine_district.xy_chine_district"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xy_chine_district.object', {
#             'object': obj
#         })
