# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_invoice_analytic_search = fields.Boolean(string='account invoice analytic search',
        help='Organizations often require to quickly find the invoices associated to a \n'
              'project or to an analytic account, searching by its code or name. \n'
              'This module introduces the possibility search customer or supplier \n'
              'invoices by analytic account. \n'
             '-This installs the module account_invoice_analytic_search.')
    
    module_account_invoice_anglo_saxon_no_cogs_deferral = fields.Boolean(string='account invoice anglosaxon no cogsdeferral',
        help='This module invalidates the COGS deferral introduced by the Anglo Saxon'
              'Accounting module. \n' )

    module_account_invoice_blocking = fields.Boolean(string='account invoice blocking',
        help='This module allows the user to set a blocking (No Follow-up) flag directly on the invoice.'
              'This facilitates the blocking of the invoices move lines. \n' )

    module_account_invoice_change_currency = fields.Boolean(string='account invoice change currency',
        help='This module allows users to update the currency of Invoices (in draft state) by \n'
              'a button Update Currency at the invoice form. \n'
              'After update to new currency, all the unit prices of invoice lines will be \n'
              'recomputed to new currency, thus the Total amounts (tax and without tax) of \n'
              'Invoice will be in the new currency also \n'

              'Also this module allows user to set a custom rate that will be take to recompute \n'
              'all lines. By default the custom rate proposed is the rate between invoice \n'
              'currency and base currency (company currency), after the first coversion the \n'
              'custom rate will be proposed by default between last currency and invoice \n'
              'currency.'
             '-This installs the module account_invoice_change_currency.')


    module_account_invoice_check_total = fields.Boolean(string='account invoice check total',
        help=' Add a Verification Total field on vendor bills. \n'
              'The user enters the taxes included invoice total as printed on the vendor bill, \n'
              'then enters the invoice lines and taxes. \n'
              'The system then checks the total computed by Odoo is the same as the verification total. \n'
             '-This installs the module account_invoice_check_total .')

    module_account_invoice_fiscal_position_update = fields.Boolean(string='account invoice fiscal position update',
        help='With this module, when a user changes the fiscal position of an invoice, the \n'
              'taxes and the accounts on all the invoice lines which have a product are \n'
              'automatically updated. The invoice lines without a product are not updated and \n'
              'a warning is displayed to the user in this case. \n'
            '-This installs the module account_invoice_fiscal_position_update .')

    module_account_invoice_fixed_discount = fields.Boolean(string='account invoice fixed discount',
        help='This module extends the functionality of Invoicing to allow you to apply fixed \n'
              'amount discounts at invoice line level. \n'
              'The module also extends the invoice report to show fixed discount. \n'  
              '-This installs the module account_invoice_fixed_discount .')

    module_account_invoice_force_number = fields.Boolean(string='account_invoice_force_number',
        help='This module allows to force the invoice numbering. It displays the move_name field. \n'
             'If user fills that field, the typed value will be used as invoice (and move) number. \n' 
             'Otherwise, the next sequence number will be retrieved and saved.  \n'
             'So, the new field has to be used when user doesnt want to use the default invoice numbering for a specific invoice. \n'
             '-This installs the module account_invoice_force_number .')

    module_account_invoice_line_description = fields.Boolean(string='account invoice-line description',
        help='This module allows to use only the sale description or the purchase description \n'
              'on the invoice lines depending on the invoice type. \n'
             '-This installs the module account_invoice_line_description .')

    module_account_invoice_line_sequence = fields.Boolean(string='account_invoice_line_sequence',
        help='Provides a new sequence field on invoice lines which helps to manage the order of the invoice lines. \n'
             '-This installs the module account_invoice_line_sequence .')

    module_account_invoice_pricelist = fields.Boolean(string='account_invoice_pricelist',
        help='* Add a stored field pricelist on invoices, related to the partner pricelist; \n'
              '* Use this pricelist when manually adding invoice lines \n'
              '* Possibility to group by pricelist on account.invoice view; \n'
             '-This installs the module account_invoice_pricelist .')


    module_account_invoice_refund_link = fields.Boolean(string='account invoice refund-link',
        help='This module creates in the invoice form a new Refunds page when the invoice \n'
              'has some refunds. It shows a line for each refund invoice with main \n'
              'information. \n'
             '-This installs the module account_invoice_refund_link .')

    module_account_invoice_reimbursable = fields.Boolean(string='account invoice reimbursable',
        help='This module adds the option to add reimbursables to supplier invoices. \n'
              'Reimbursables are payments for services that your supplier has made on behalf'
              'of your company as part of an agreement. \n'
              'Your company receives two invoices: one from the supplier, that includes'
              'the reimbursable, and your company should pay, and one from the third party'
              'that has been paid by your supplier on your behalf. \n'

              'For example, when you set up a company your lawyer might pay for various'
              'government fees on your behalf, that the lawyer is then going to pass on to you'
              'as a reimbursable in the invoice. You will still receive an invoice for the'
              'government fees, but you have no obligation to pay them, because they have'
              'already been paid by your lawyer. \n'
             '-This installs the module account_invoice_reimbursable .')

    module_account_invoice_repair_link = fields.Boolean(string='account_invoice_repair_link',
        help='This module adds a link between invoices and repair orders. Invoices are generated from'
              'the repair orders. With this module you can navigate back to the repair orders that'
              'generated a specific invoice. \n'
              'This module is useful if you want to add information from the repair in the invoice report. \n'
             '-This installs the module account_invoice_repair_link .')

    module_account_invoice_search_by_reference = fields.Boolean(string='account invoice search by reference',
        help='This module adds the ability of searching by vendor reference when searching'
              'invoices from different views. This is useful for example, when receiving'
              'supplier RMAs, where the user can search only by the internal invoice number. \n'
              '-This installs the module account_invoice_search_by_reference .')

    module_account_invoice_supplier_ref_reuse = fields.Boolean(string='account invoice supplier refreuse',
        help='In some cases, having more than one supplier invoice with the same'
              'reference is possible. For instance, in Switzerland, BVR/ESR numbers'
              'are used as a type of reference. Generally, this number is unique and'
              'used only for one invoice. However, some suppliers do use the same BVR'
              'reference for several invoices (usually for recurring invoices). \n'
             '-This installs the module account_invoice_supplier_ref_reuse .')

    module_account_invoice_supplier_ref_unique = fields.Boolean(string='account invoice supplier ref-unique',
        help='This module checks that a supplier invoice/refund is not entered twice. \n'
               'This is important because if you enter twice the same supplier invoice,' 
               'there is also a risk that you pay it twice ! \n'
              'This module adds a constraint on supplier invoice/refunds to check that (commercial_partner_id, supplier_invoice_number) is unique, '
              'without considering the case of the supplier invoice number. \n'
             '-This installs the module account_invoice_supplier_ref_unique .')

    module_account_invoice_supplierinfo_update = fields.Boolean(string='account invoice supplierinfo update',
        help='This module allows to automatically update all products information in vendor bill for '
              'which the purchase information on the line are different from the supplier information defined in the product form. \n'
              'It creates a new supplier information line if there is not any or it updates the first one in the list. \n'
             '-This installs the module account_invoice_supplierinfo_update .')


    module_account_invoice_tax_note = fields.Boolean(string='account invoice tax-note',
        help='In some situations, a mention must be displayed on invoices when a specific tax is used. \n'
            'This module lets you define such a mention on Tax Groups. \n'
            'This mechanism complements the invoice note coming from the fiscal position. \n'
            'These tax group notes are translatable and company dependent. \n'
            'To contribute to this module, please visit https://odoo-community.org. \n'
             '-This installs the module account_invoice_tax_note .')

    module_account_invoice_tax_required = fields.Boolean(string='account invoice tax-required',
        help='This module adds functional a check on invoice'
              'to force user to set tax on invoice line. \n'
             '-This installs the module account_invoice_tax_required .')

    module_account_invoice_transmit_method = fields.Boolean(string='account invoice transmit-method',
        help= 'This module allows to configure an *Invoice Transmit Method* on each partner.'
               ' This module provides by default 3 transmission methods: \n'
              '* E-mail \n'
              '* Post \n'
              '* Customer Portal \n'
              'You can manually create additionnal transmission methods or other modules can create '
              'additionnal transmission methods (for example, '
              'the  module *l10n_fr_chorus* creates a specific transmission method *Chorus*, '
              'which is the e-invoicing plateform of the French  administration). \n'
             '-This installs the module account_invoice_transmit_method .')

    module_account_invoice_triple_discount = fields.Boolean(string='account invoice triple discount',
        help='This module allows to have three successive discounts on each invoice line. \n')

    module_account_invoice_view_payment = fields.Boolean(string='account invoice view-payment',
        help='This module allows users to access directly to the payment from an invoice \n'
              'when registering a payment or afterwards. \n'

              'The option to open the payment when its being registered is useful \n'
              'when the user needs to do a follow-up step on the payment, such as printing \n'
              'the associated check. \n'
             '-This installs the module account_invoice_view_payment .')

   
    module_account_menu_invoice_refund = fields.Boolean(string='account menu invoice refund',
        help='This module add 2 new menus, \n'
              '1. Invoicing > Customers > Invoices / Credit Notes \n'
              '2. Invoicing > Vendors > Bills / Refunds \n'
              'Additionally it allow register net payment by selecting both invoice and refund. \n'
             '-This installs the module account_menu_invoice_refund .')

    module_account_payment_term_extension = fields.Boolean(string='account payment term extension',
        help='This module extends the functionality of payment terms to : \n'
            '* support rounding, months and weeks on payment term lines \n'
            '* allow to set more than one day of payment in payment terms \n'
            '* if a payment term date is a holiday, it is postponed to a selected date \n'
            '* allow to apply a chronological order on lines \n'
              '* for example, with a payment term which contains 2 lines \n'

                '* on standard, the due date of all lines is calculated from the invoice \n'
                '  date \n'
                '* with this feature, the due date of the second line is calculated from \n'
                '  the due date of the first line \n'
             '-This installs the module account_payment_term_extension .')

    module_purchase_batch_invoicing = fields.Boolean(string='purchase_batch_invoicing',
        help='This module extends the functionality of purchases to support batch invoicing \n'
              'purchase orders and to allow you to choose if you want them grouped by purchase \n'
              'order or by vendor. \n'
             '-This installs the module purchase_batch_invoicing .')

    module_purchase_stock_picking_return_invoicing = fields.Boolean(string='purchase stock picking return invoicing',
        help='This module extends the functionality of purchase orders to better manage \n'
              'supplier returns and refunds. \n'

              'In the purchase order you are able to display, for each line: \n'

              '* Billed Quantity and Refunded Quantity, as separate fields. \n'

              '* Received Quantity and Returned Refundable Quantity, as separate fields. \n'

              'You have the option to create a vendor bill or a refund. In the bill or refund \n'
              'the correct quantity will be proposed, based on those fields. \n'
             '-This installs the module purchase_stock_picking_return_invoicing .')

    module_purchase_stock_picking_return_invoicing_force_invoiced = fields.Boolean(string='purchase stock picking return invoicing force-invoiced',
        help='This module forces the status of the purchase order to remain in Invoiced \n'
                'even when you have returned items into stock, if you indicated in the purchase \n'
                'order that you wanted to force the invoiced status. \n'

                'It is a glue module between the module Purchase Force Invoiced and \n'
                'Purchase Stock Picking Return Invoicing. \n'
             '-This installs the module purchase_stock_picking_return_invoicing_force_invoiced .')

    module_sale_invoice_line_note = fields.Boolean(string='sale invoice line note',
        help='This module adds a checkbox Copy notes to invoice in the create invoice \n'
              'wizard from the sale order, to propagate sale order line of Note type to the \n'
              'created invoice. \n'
             '-This installs the module sale_invoice_line_note .')

    module_sale_order_invoicing_queued = fields.Boolean(string='sale order invoicing queued',
        help='This module allows to enqueue in several jobs the sales orders invoicing \n'
              'process to be executed in paralell on background, which is normally done \n'
              'serially and on foreground. \n'

              'Jobs are split following the same criteria as standard Odoo: grouping by \n'
              'order invoicing address and order currency. \n'
             '-This installs the module sale_order_invoicing_queued .')

    module_sale_timesheet_invoice_description = fields.Boolean(string='sale timesheet invoice description',
        help='Add timesheet details in invoice line to invoices related with timesheets. \n'
             '-This installs the module sale_timesheet_invoice_description .')

