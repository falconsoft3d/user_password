# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class UserPassword(models.Model):
    _description = "Usuario Pass"
    _name = 'user.password'

    name = fields.Char('User')
    mypass = fields.Char('Password')