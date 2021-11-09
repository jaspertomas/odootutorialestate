# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = 'estate.property'

    create_uid = fields.Integer()
    create_date = fields.Date()
    write_uid = fields.Integer()
    write_date = fields.Date()
    name = fields.Char("Title",required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date("Available From",copy=False, default=fields.Datetime.today() + relativedelta(months=+6))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Char()
    active = fields.Boolean()

