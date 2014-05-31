
{
    "name" : "Amazon e-commerce",
    "version" : "1.0",
    "depends" : ["base","product","sale",'base_sale_multichannels','product_images_olbs'],
    "author" : "Bista Solutions",
    "description": """Amazon E-commerce management""",
    "website" : "http://www.bistasolutions.com/",
    "category" : "Generic Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
        'security/ir.model.access.csv',
            'amazon_view.xml',
            'product_view.xml',
            'partner_view.xml',
            'sale_view.xml',
            'amazon_menu.xml',
            'wizard/create_amazon_shop.xml',
            'ecomm_sett.xml',
            'category_attribute.xml',
            'wizard/amazon_product_lookup.xml',
            'product_images_view.xml',
            'magento_sale.xml'
                    ],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

