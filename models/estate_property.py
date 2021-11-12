# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = 'estate.property.offer'

    price = fields.Float()
    status = fields.Selection([("A", "Accepted"), ("R", "Refused")],copy=False)
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    property_id = fields.Many2one("estate.property", string="Property")

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = 'estate.property.tag'

    name = fields.Char(required=True)

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'estate.property.type'

    name = fields.Char(required=True)
    description = fields.Text()

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
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesman_id = fields.Many2one("res.users", string="Salesman",default=lambda self: self.env.uid, copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
