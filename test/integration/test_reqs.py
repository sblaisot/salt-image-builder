import pytest


@pytest.mark.parametrize(
    "cmd",
    ["python", "pip"],
)
def test_python(host, pyvers, cmd):
    if pyvers == "2":
        python_verstr = ''
    else:
        python_verstr = pyvers
    host.find_command(cmd + python_verstr)


@pytest.mark.parametrize(
    "cmd",
    ["git", "netstat", "ps"],
)
def test_reqs(host, cmd):
    host.find_command(cmd)
