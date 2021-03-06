#
# Copyright (C) 2019 Red Hat, Inc
# see the LICENSE file for license
#

import pkg_resources
import requests
from omps import __version__ as version


def test_about(client):
    """Test /about endpoint"""

    rv = client.get('/v2/about')

    assert rv.status_code == requests.codes.ok
    assert rv.get_json() == {
        'version': version,
        'operatorcourier': pkg_resources.get_distribution('operator-courier').version,
    }
