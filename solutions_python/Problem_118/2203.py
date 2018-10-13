from nose.tools import raises, eq_
from cj import *

def is_fair_test():
    assert(is_fair(0) == True)
    assert(is_fair(1) == True)
    assert(is_fair(2) == True)
    assert(is_fair(3) == True)
    assert(is_fair(4) == True)
    assert(is_fair(11) == True)
    assert(is_fair(121) == True)
    assert(is_fair(1221) == True)
    assert(is_fair(12321) == True)
    assert(is_fair(123321) == True)
    assert(is_fair(1234321) == True)
    assert(is_fair(12345678900987654321) == True)
    assert(is_fair(1234567890098765432112345678900987654321) == True)

    assert(is_fair(10) == False)
    assert(is_fair(12) == False)
    assert(is_fair(223) == False)
    assert(is_fair(2244) == False)
    assert(is_fair(123) == False)
    assert(is_fair(12331) == False)
    assert(is_fair(21111111111111111111111111111111111111111111111111) == False)

def is_square_test():
    assert(is_square(1) == True)
    assert(is_square(4) == True)
    assert(is_square(9) == True)
    assert(is_square(16) == True)
    assert(is_square(121) == True)

    assert(is_square(2) == False)
    assert(is_square(3) == False)
    assert(is_square(5) == False)
    assert(is_square(99) == False)
    assert(is_square(100) == False)
    assert(is_square(676) == False)
