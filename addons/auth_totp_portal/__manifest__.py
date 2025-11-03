{
    'name': "TOTPortal",
    'category': 'Hidden',
    'depends': ['portal', 'auth_totp'],
    'data': [
        'security/security.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'auth_totp_portal/static/src/**/*',
        ],
        'web.assets_tests': [
            'auth_totp_portal/static/tests/**/*',
        ],
    },
    'license': 'LGPL-3',
}
