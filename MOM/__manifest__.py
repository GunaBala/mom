#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Minutes Of Meeting',
    'version': '12.0.0.0.1',
    'author':'Gunasekaran'
    'license':'LGPL-3',
    'category': 'Sale',
    'sequence': 40,
    'summary': 'Manage your Minutes of meeting',
    'description': "",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/mom_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application':True,
    'auto_install': False,
    'certificate': '',
}
