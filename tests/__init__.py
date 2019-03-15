# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.party_ar.tests.tests import suite
except ImportError:
    from .tests import suite

__all__ = ['suite']
