# -*- coding: utf-8 -*-
from odoo import http

# class Myshop1(http.Controller):
#     @http.route('/myshop1/myshop1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myshop1/myshop1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myshop1.listing', {
#             'root': '/myshop1/myshop1',
#             'objects': http.request.env['myshop1.myshop1'].search([]),
#         })

#     @http.route('/myshop1/myshop1/objects/<model("myshop1.myshop1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myshop1.object', {
#             'object': obj
#         })