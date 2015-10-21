# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2015 Florian Bruhin (The Compiler) <mail@qutebrowser.org>:
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for KeyParser."""

import sys
import logging
from unittest import mock

from PyQt5.QtCore import Qt
import pytest

from qutebrowser.keyinput import keyparser
from qutebrowser.keyinput import basekeyparser
from qutebrowser.utils import utils

CONFIG = {'input': {'timeout': 100}}

class test_keyparser():

    def test_init():
        kp = basekeyparser.BaseKeyParser(
            0, supports_count=True, supports_chains=True)
        kp.execute = mock.Mock()
        ckp = new CommandKeyParser(kp)
