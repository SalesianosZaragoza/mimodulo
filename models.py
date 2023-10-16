from odoo import models, fields, api

class ventas(models.Model):
    _name = 'ventas_cole.ventas'
    _description = 'ventas_cole.ventas'
    name = fields.Char()
    descripcion = fields.Char()
    precio = fields.Integer()
    cantidad = fields.Integer()
    total = fields.Integer()
    cliente = fields.Char()
    vendedor = fields.Many2one(comodel_name='ventas_cole.vendedores')
    factura = fields.Char()
    fecha = fields.Date()
    total_con_decimales = fields.Float()

class vendedores(models.Model):
    _name = 'ventas_cole.vendedores'
    _description = 'ventas_cole.vendedores'
    _rec_name = 'nombre' # Para que se muestre el nombre en lugar del id
    nombre = fields.Char()
    apellido = fields.Char()
    dni = fields.Char()
    ventas = fields.One2many(comodel_name='ventas_cole.ventas', inverse_name='vendedor')