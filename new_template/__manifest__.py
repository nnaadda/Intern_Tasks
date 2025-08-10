{
    'name': 'Simple Custom Layout',
    'version': '18.0.1.0.0',
    'category': 'Reporting',
    'summary': 'Simple Custom Report Layout for Odoo 18',
    'description': 'Adds a new custom layout option to document configuration',
    'depends': ['base', 'web'],
    'data': [
        'views/report_layout.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}