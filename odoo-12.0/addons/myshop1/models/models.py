# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ManufacturerShop(models.Model):
    _name = 'manufacturer.shop1'
    _description = 'Manufacturer Shop'
    _rec_name = 'manufacturer'

    manufacturer = fields.Char(required=True, index=True, help='Manufacturer of product', string='Manufacturer')


class ModelShop(models.Model):
    _name = 'model.shop1'
    _description = 'Model Shop'
    _rec_name = 'model_phone'

    model_phone = fields.Char(required=True, help='Model of product', string='Model')
    manufacturer_id = fields.Many2one('manufacturer.shop1', ondelete='cascade', required=True)


class SaleProductInherit(models.Model):
    _inherit = 'product.template'

    manufacturer_id = fields.Many2one('manufacturer.shop1')
    model_id = fields.Many2one('model.shop1')
