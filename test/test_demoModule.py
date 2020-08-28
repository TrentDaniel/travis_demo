import pytest
from demoPackage.demoModule import *

def test_add():
    assert add(1, 2) == 3, "adding 1 and 2 should result in 3"

def test_sub():
    assert sub(10, 3) == 7, "subtracting 5 from 10 should return 7"

def test_get_sys_path():
    print("sys.path is: ", get_sys_path())
    assert get_sys_path() is not None, "sys.path should not be None"

def test_get_platform():
    print(get_platform())
    assert get_platform is not None, "platform.system() should not be None"
