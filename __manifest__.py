# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "TN Invoice Report",
    'summary': """Invoice with stamp   """,
    'description': """
        Invoice conforming to Tunisian standard, with tax stamp (Timbre Fiscal)
    """,
    'license': 'AGPL-3',
    'author': "	AHMED MNASRI",
    'website': "",
    'category': 'Accounting',
    'version': '12.0.0.2.0',
    'depends': ['account',
                'timbre_fiscal',
                ],
    'data': [
        'report/invoice_report_template.xml',
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
