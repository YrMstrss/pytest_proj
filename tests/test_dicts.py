import pytest
from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


def test_get_val():
    assert dicts.get_val(data(), "vcs", 'git') == "mercurial"
    assert dicts.get_val(data(), "vcs") == "mercurial"
    assert dicts.get_val({}, "vcs", 'git') == 'git'
    assert dicts.get_val({}, "vcs", 'Pupa') == 'Pupa'
