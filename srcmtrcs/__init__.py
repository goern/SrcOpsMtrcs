#!/usr/bin/env python3
# SrcMtrcs
# Copyright(C) 2018 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""This is Source Operations Metrics..."""

import os
from flask import Flask

from .webhooks import webhooks
from .metrics import metrics
from .humans import website
from .probes import probes


__name__ = 'srcmrtcs'
__version__ = "0.1.0"
__author__ = 'Christoph Görn <goern@redhat.com>'


def create_application():
    """Create, configure and return the Flask application."""
    app = Flask(__name__)
    app.config['GITHUB_WEBHOOK_SECRET'] = os.environ.get(
        'GITHUB_WEBHOOK_SECRET')

    app.register_blueprint(webhooks)
    app.register_blueprint(metrics)
    app.register_blueprint(probes)
    app.register_blueprint(website)

    return(app)
