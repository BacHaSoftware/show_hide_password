# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Show/Hide Password',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'category': 'Extra Tools',
    'summary': """
        Show/Hide Password in login screen, View Password Login Page, Show Password Login Page, Hide Password Login Page, Web Responsive login, Odoo Web Login Page, Web backend login, Odoo login,
        Show/Hide Password in sign in screen, View Password SignIn Page, Show Password SignUp Page, Hide Password SignIn Page, Web Responsive SignIn, Odoo Web SignIn Page, Web backend SignIn, Odoo SignUp Page, Odoo SignIn Page
    """,
    'description': "You can show and hide your password in login screen.",
    'author': 'Bac Ha Software',
    'company': 'Bac Ha Software',
    'maintainer': 'Bac Ha Software',
    'website': "https://bachasoftware.com",
    'license': 'LGPL-3',
    'depends': [
        'web'
    ],
    'data': [
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'bhs_show_hide_password/static/src/scss/login.scss',
        ],
    },
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
