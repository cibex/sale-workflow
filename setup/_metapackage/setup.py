import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-sale-workflow",
    description="Meta package for oca-sale-workflow Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-partner_contact_sale_info_propagation>=15.0dev,<15.1dev',
        'odoo-addon-partner_sale_pivot>=15.0dev,<15.1dev',
        'odoo-addon-portal_sale_personal_data_only>=15.0dev,<15.1dev',
        'odoo-addon-pricelist_cache>=15.0dev,<15.1dev',
        'odoo-addon-product_form_sale_link>=15.0dev,<15.1dev',
        'odoo-addon-product_supplierinfo_for_customer_elaboration>=15.0dev,<15.1dev',
        'odoo-addon-product_supplierinfo_for_customer_sale>=15.0dev,<15.1dev',
        'odoo-addon-sale_advance_payment>=15.0dev,<15.1dev',
        'odoo-addon-sale_attached_product>=15.0dev,<15.1dev',
        'odoo-addon-sale_automatic_workflow>=15.0dev,<15.1dev',
        'odoo-addon-sale_automatic_workflow_job>=15.0dev,<15.1dev',
        'odoo-addon-sale_automatic_workflow_payment_mode>=15.0dev,<15.1dev',
        'odoo-addon-sale_blanket_order>=15.0dev,<15.1dev',
        'odoo-addon-sale_cancel_reason>=15.0dev,<15.1dev',
        'odoo-addon-sale_commercial_partner>=15.0dev,<15.1dev',
        'odoo-addon-sale_credit_point>=15.0dev,<15.1dev',
        'odoo-addon-sale_custom_rounding>=15.0dev,<15.1dev',
        'odoo-addon-sale_delivery_split_date>=15.0dev,<15.1dev',
        'odoo-addon-sale_delivery_state>=15.0dev,<15.1dev',
        'odoo-addon-sale_discount_display_amount>=15.0dev,<15.1dev',
        'odoo-addon-sale_elaboration>=15.0dev,<15.1dev',
        'odoo-addon-sale_exception>=15.0dev,<15.1dev',
        'odoo-addon-sale_fixed_discount>=15.0dev,<15.1dev',
        'odoo-addon-sale_force_invoiced>=15.0dev,<15.1dev',
        'odoo-addon-sale_force_whole_invoiceability>=15.0dev,<15.1dev',
        'odoo-addon-sale_fully_invoiced>=15.0dev,<15.1dev',
        'odoo-addon-sale_global_discount>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoice_blocking>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoice_frequency>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoice_no_mail>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoice_plan>=15.0dev,<15.1dev',
        'odoo-addon-sale_invoice_policy>=15.0dev,<15.1dev',
        'odoo-addon-sale_isolated_quotation>=15.0dev,<15.1dev',
        'odoo-addon-sale_last_price_info>=15.0dev,<15.1dev',
        'odoo-addon-sale_missing_tracking>=15.0dev,<15.1dev',
        'odoo-addon-sale_missing_tracking_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_archive>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_carrier_auto_assign>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_discount_invoicing>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_general_discount>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_invoice_amount>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_invoicing_finished_task>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_chained_move>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_date>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_delivery_state>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_description>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_input>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_menu>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_note>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_price_history>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_remove>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_line_sequence>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_lot_selection>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_partner_no_autofollow>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_partner_restrict>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_price_recalculation>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_priority>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_product_assortment>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_product_availability_inline>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_product_recommendation>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_product_recommendation_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_qty_change_no_recompute>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_report_without_price>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_restrict_cancel_existing_invoice>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_revision>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_type>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_type_quotation_number>=15.0dev,<15.1dev',
        'odoo-addon-sale_order_warn_message>=15.0dev,<15.1dev',
        'odoo-addon-sale_partner_incoterm>=15.0dev,<15.1dev',
        'odoo-addon-sale_partner_selectable_option>=15.0dev,<15.1dev',
        'odoo-addon-sale_payment_sheet>=15.0dev,<15.1dev',
        'odoo-addon-sale_planner_calendar>=15.0dev,<15.1dev',
        'odoo-addon-sale_pricelist_global_rule>=15.0dev,<15.1dev',
        'odoo-addon-sale_procurement_group_by_commitment_date>=15.0dev,<15.1dev',
        'odoo-addon-sale_procurement_group_by_line>=15.0dev,<15.1dev',
        'odoo-addon-sale_product_category_menu>=15.0dev,<15.1dev',
        'odoo-addon-sale_product_multi_add>=15.0dev,<15.1dev',
        'odoo-addon-sale_product_set>=15.0dev,<15.1dev',
        'odoo-addon-sale_product_set_layout>=15.0dev,<15.1dev',
        'odoo-addon-sale_purchase_procurement_group_by_line>=15.0dev,<15.1dev',
        'odoo-addon-sale_quotation_number>=15.0dev,<15.1dev',
        'odoo-addon-sale_readonly_security>=15.0dev,<15.1dev',
        'odoo-addon-sale_rental>=15.0dev,<15.1dev',
        'odoo-addon-sale_resource_booking>=15.0dev,<15.1dev',
        'odoo-addon-sale_shipping_info_helper>=15.0dev,<15.1dev',
        'odoo-addon-sale_sourced_by_line>=15.0dev,<15.1dev',
        'odoo-addon-sale_start_end_dates>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_cancel_restriction>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_delivery_address>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_invoice_plan>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_last_date>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_line_sequence>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_picking_blocking>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_picking_note>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_return_request>=15.0dev,<15.1dev',
        'odoo-addon-sale_stock_secondary_unit>=15.0dev,<15.1dev',
        'odoo-addon-sale_substate>=15.0dev,<15.1dev',
        'odoo-addon-sale_tier_validation>=15.0dev,<15.1dev',
        'odoo-addon-sale_triple_discount>=15.0dev,<15.1dev',
        'odoo-addon-sale_validity_auto_cancel>=15.0dev,<15.1dev',
        'odoo-addon-sale_warn_option>=15.0dev,<15.1dev',
        'odoo-addon-sale_wishlist>=15.0dev,<15.1dev',
        'odoo-addon-sales_team_security>=15.0dev,<15.1dev',
        'odoo-addon-sales_team_security_crm>=15.0dev,<15.1dev',
        'odoo-addon-sales_team_security_sale>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
