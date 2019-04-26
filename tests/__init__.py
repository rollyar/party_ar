# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.party_ar.tests.test_party_ar import suite
except ImportError:
    from .test_party_ar import suite

__all__ = ['suite']
