import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from codigo import sumar

def test_sumar():
    assert sumar(2, 3) == 5