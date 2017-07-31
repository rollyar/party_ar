# This file is part of the party_ar module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pool import Pool
from . import party
from . import address


def register():
    Pool.register(
        party.AFIPVatCountry,
        party.Party,
        party.PartyIdentifier,
        party.GetAFIPDataStart,
        address.Address,
        module='party_ar', type_='model')
    Pool.register(
        party.GetAFIPData,
        module='party_ar', type_='wizard')
