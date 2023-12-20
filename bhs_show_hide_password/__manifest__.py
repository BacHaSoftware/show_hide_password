# -*- coding: utf-8 -*-
{
  'name': 'Show/Hide Password',
  "summary":  """view password at login and signup page.""",
  "category":  "Website",
  "version":  "17.0",
  'author': 'Bac Ha Software',
  'company': 'Bac Ha Software',
  'maintainer': 'Bac Ha Software',
  'website': "https://bachasoftware.com",
  "description":  "You can show and hide your password in login screen.",
  "depends":  ['web'],
  "data":  ['views/auth_signup_login.xml'],
  'images': ['static/description/banner.jpg'],
  "application":  True,
  "installable":  True,
  "auto_install":  False,
  'assets': {
      'web.assets_frontend': [
          'bhs_show_hide_password/static/src/scss/bhs_show_hide_password.scss',
          'bhs_show_hide_password/static/src/js/bhs_show_hide_password.js',
      ],
  },
  "pre_init_hook":  "pre_init_check",
  'license': 'LGPL-3'
}
