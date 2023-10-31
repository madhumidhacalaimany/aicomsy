# -*- coding: utf-8 -*-


{
    'name': 'Incident Management',
    'depends': [
        'base', 'hr', 'maintenance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/incident_record_views.xml',
        'views/inc_person_views.xml',
        'views/inc_asset_views.xml',
        'views/inc_spills_views.xml',
        'views/inc_inv_corrective_actions_views.xml',
        'views/inc_consequences_views.xml',
        'views/inc_investigation_people_views.xml',
        'views/inc_root_causes_views.xml',
        'views/inc_action_review_closure_views.xml',
        'views/inc_investigation_views.xml',
        'views/inc_lov_views.xml',
        'views/inc_consequences_lov_views.xml',
        'views/inc_corrective_actions_lov_views.xml',
        'views/incident_management_menu.xml',
        'data/mail_template_data.xml',
        'data/incident_type_data.xml',
        'data/incident_person_category_data.xml',
        'data/incident_injury_type_data.xml',
        'data/incident_injured_body_parts_data.xml',
        'data/incident_person_immediate_response_data.xml',
        'data/incident_asset_immediate_response_data.xml',
        'data/x_inc_spill_immediate_response_data.xml',
        'data/incident_shift_data.xml',
        'data/x_inc_hierarchy_control_data.xml',
        'data/x_inc_location_data.xml',
        'data/x_inc_oh_classification_data.xml',
        'data/x_inc_unit_data.xml',
        'data/x_inc_action_type_data.xml',
        'data/x_inc_action_damage_data.xml',
        'data/x_inc_env_classification_data.xml',
        'data/x_inc_env_impact_data.xml',
        'data/x_inc_rootcause_data.xml',
        'data/x_inc_oh_severity_classifications_data.xml',
        'data/x_inc_oh_severity_consequence_data.xml',
        'data/x_inc_env_severity_classification_data.xml',
        'data/x_inc_env_severity_consequence_data.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'incident_management/static/src/scss/custom_style.scss',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
