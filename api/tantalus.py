"""Tantalus api blueprint gen"""
from flask import Blueprint

blueprints = []


def blueprint_factory(partial_module_string, url_prefix):
    """Generates blueprint objects for view modules.

    Positional arguments:
    partial_module_string -- string representing a view module without the absolute path
    url_prefix -- URL prefix passed to the blueprint.

    Returns:
    Blueprint instance for a view module.
    """
    name = partial_module_string
    import_name = 'api.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    blueprints.append(blueprint)
    return blueprint


# Create blueprints, can be imported by views
bp_base = blueprint_factory("tantalus", '')
bp_product = blueprint_factory("tantalus.product", '/product')
bp_mod = blueprint_factory("tantalus.mod", '/mod')
bp_relation = blueprint_factory('tantalus.relation', '/relation')
bp_transaction = blueprint_factory('tantalus.transaction', '/transaction')
bp_user = blueprint_factory('tantalus.user', '/user')
bp_pos = blueprint_factory('tantalus.pos', '/pos')

# Import modules to make them register, this needs to be after the blueprint definition
# Otherwise you get an unresolvable circular import

import mod, product, base, transaction, relation, user, pos
