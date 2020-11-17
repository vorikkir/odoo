# -*- coding: utf-8 -*-

from odoo import api, fields, models
from pprint import pprint

class ManufacturerShop(models.Model):
    _name = 'manufacturer.shop1'
    _description = 'Manufacturer Shop1'
    _rec_name = 'manufacturer'

    manufacturer = fields.Char(required=True, index=True, help='Manufacturer of product', string='Manufacturer1')
    # model_id = fields.One2many('model.shop1', 'manufacturer_id')


class ModelShop(models.Model):
    _name = 'model.shop1'
    _description = 'Model Shop1'
    _rec_name = 'model_phone'

    model_phone = fields.Char(required=True, help='Model of product', string='Model1')
    manufacturer_id = fields.Many2one('manufacturer.shop1',  ondelete='cascade', required=True)


class SaleProductInherit(models.Model):
    _inherit = "product.template"

    def _manufacturer_field_get(self):
        mf = self.env['manufacturer.shop1'].search([])
        res = []
        for field in mf:
            res.append((field.manufacturer, field.manufacturer))
        return res

    def _model_phone_field_get(self):

        mf = self.env['model.shop1'].search([])
        res = []
        for field in mf:
            res.append((field.model_phone, field.model_phone))
        return res




    @api.onchange('manufacturer')
    def _check_manufacturer_field_get(self):
        result = []
        if self.manufacturer:
            id_manufacturer = self.env['manufacturer.shop1'].search([('manufacturer', '=', self.manufacturer)]).id
            model_from_manufacturer = self.env['model.shop1'].search([('manufacturer_id', '=', id_manufacturer)])
            # print('self.manufacturer..........', id_manufacturer)
            # print('self.manufacturer..........', model_from_manufacturer)
            # if self.manufacturer == 'Samsung':
            for rec in model_from_manufacturer:
                result.append((rec.model_phone, rec.model_phone))

                print('rec', rec.model_phone.model_phone)




    model_phone = fields.Selection(_model_phone_field_get, 'Phone model')
    manufacturer = fields.Selection(_manufacturer_field_get, 'Manufacturer')