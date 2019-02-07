from odoo import api, fields, models
from datetime import date

class minutes_of_meeting(models.Model):
    _name = "minutes.of.meeting"
    
    user_id = fields.Many2one('res.users',"User",default=lambda self: self.env.user.id)
    name = fields.Char('Description')
    date=fields.Date("Expiry Date")
    

   
