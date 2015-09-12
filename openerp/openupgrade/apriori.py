""" Encode any known changes to the database here
to help the matching process
"""

from openerp.openupgrade import openupgrade

renamed_modules = {
    # 'base_calendar': 'calendar',
    # 'mrp_jit': 'procurement_jit',
    # # OCA/account-invoicing
    # 'invoice_validation_wkfl': 'account_invoice_validation_workflow',
    # 'account_invoice_zero': 'account_invoice_zero_autopay',
    # # OCA/server-tools
    # 'audittrail': 'auditlog',
    # # OCA/bank-statement-import
    # 'account_banking': 'account_bank_statement_import',
    # 'account_banking_camt': 'bank_statement_parse_camt',
    # 'account_banking_nl_ing_mt940': 'bank_statement_parse_nl_ing_mt940',
    # 'account_banking_nl_rabo_mt940': 'bank_statement_parse_nl_rabo_mt940',
    'l10n_co_base': 'l10n_co_geo',
    'l10n_co_razonsocial': 'l10n_co_terceros',
    #'l10n_co_dian_auth': 'l10n_co_terceros',
    'l10n_co_retenciones': 'l10n_co_core',
}

renamed_models = {
}

module_names_merge = {
    'l10n_co_dian_auth': 'l10n_co_terceros',
}

def migrate_apriori(cr):
    openupgrade.update_module_names(
        cr, renamed_modules.iteritems()
    )
    openupgrade.merge_module_names(
        cr, module_names_merge.iteritems()
    )