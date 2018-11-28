'''
Created on May 8, 2010

@author: psyho
'''
import unittest
import fractions

def gcd(list_of_integers):
    if len(list_of_integers) == 0: return 1
    if len(list_of_integers) == 1: return list_of_integers[0]
    
    result = fractions.gcd(list_of_integers[0], list_of_integers[1])
    
    for i in list_of_integers[2:]:
        result = fractions.gcd(result, i)
    
    return result


def fair_warning(great_events):
    maximum = max(great_events)
    normalised = [maximum - i for i in great_events]
    T = gcd(normalised)
    if maximum % T == 0: return 0
    return (maximum // T + 1) * T - maximum
    

def main():
    C = int(raw_input())
    for i in range(C):
        ints = map(int, raw_input().split())
        great_events = ints[1:]
        print "Case #%d: %d" % (i+1, fair_warning(great_events))
        
if __name__ == "__main__":
    main()
    

class TestGcd(unittest.TestCase):
    
    def test_empty(self):
        self.assertEqual(1, gcd([]))
        
    def test_single(self):
        self.assertEqual(10, gcd([10]))
        
    def test_two(self):
        self.assertEqual(3, gcd([6, 15]))

    def test_more(self):
        self.assertEqual(5000, gcd([0, 15000, 20000]))

class Test(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(4000000, fair_warning([26000000, 11000000, 6000000]))
        
    def test_example_2(self):
        self.assertEqual(0, fair_warning([1, 10, 11]))

    def test_example_3(self):
        self.assertEqual(99999999999999999999, fair_warning([800000000000000000001, 900000000000000000001]))
