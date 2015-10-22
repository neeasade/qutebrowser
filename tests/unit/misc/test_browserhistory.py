# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2015 Florian Bruhin (The-Compiler) <me@the-compiler.org>
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

"""Tests for qutebrowser.browser.History."""

import pytest

import qutebrowser.browser.history

from unittest import mock

from qutebrowser.misc import cmdhistory
from qutebrowser.browser.history import WebHistory
from qutebrowser.browser.history import HistoryEntry
from PyQt5.QtCore import QUrl
import datetime

from qutebrowser.browser import cookies
from qutebrowser.utils import objreg
from qutebrowser.misc import lineparser, savemanager

# autouse fixtures (so no need to pass to tests)
# @pytest.yield_fixture(autouse=True)

HISTORY = ['first', 'second', 'third', 'fourth', 'fifth']

CONFIG_NOT_PRIVATE = {'general': {'private-browsing': False}}
CONFIG_PRIVATE = {'general': {'private-browsing': True}}

@pytest.yield_fixture(autouse=True)
def fake_save_manager():
    """Create a mock of save-manager and register it into objreg."""
    fake_save_manager = mock.Mock(spec=savemanager.SaveManager)
    objreg.register('save-manager', fake_save_manager)
    yield
    objreg.delete('save-manager')


def test_contained(qapp, config_stub, monkeypatch):
    """ Test historyContains() """
    config_stub.data = CONFIG_NOT_PRIVATE

    wb = WebHistory()
    #monkeypatch.setattr(wb, '_lineparser', LineparserSaveStub)
    lp = LineparserSaveStub(None, 'temp.stub')
    monkeypatch.setattr(wb, '_lineparser', lp)

    #entry = HistoryEntry('1444397977', 'http://asdf.com')
    wb.addHistoryEntry('http://asdf.com')
    wb.save()

    result = wb.historyContains('http://asdf.com')
    assert result == True


class LineparserSaveStub(lineparser.BaseLineParser):
    """A stub for LineParser's save()
    Attributes:
        data: The data before the write
        saved: The .data before save()
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saved = []
        self.data = []

    def save(self):
        self.saved = self.new_data

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, key):
        return self.data[key]
