{
    'name': 'Custom Banner',
    'version': '1.0',
    'depends': ['web'],
    'data': ['views/banner_template.xml'],
    'assets': {
        'web.assets_backend': [
            'custom_banner/static/src/banner.js',
        ],
    },
}
