# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _
from odoo.exceptions import AccessError

# Digest integration disabled — removed dependency on digest.digest
class Digest(models.AbstractModel):
    _name = 'account.digest.stub'
    _description = 'Stub for removed digest.digest integration'

