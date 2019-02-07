#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Minutes Of Meeting',
    'version': '12.0',
    'license':'LGPL-3',
    'category': 'Sale',
    'sequence': 40,
    'summary': 'Manage your Minutes of meeting',
    'description': "",
    'depends': ['base'],
    'images': ['images/main_screenshot.png'],
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
