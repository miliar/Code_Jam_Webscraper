'''
Created on May 8, 2010

@author: psyho
'''
import unittest

def snapper_chain(n, k):
    pow = 2 ** n
    return k % pow == pow-1

def bool_to_on_off(val):
    if val: return "ON" 
    return "OFF"

def main():
    T = int(raw_input())
    for i in range(T):
        N, K = map(int, raw_input().split())
        print "Case #%d: %s" % (i+1, bool_to_on_off(snapper_chain(N, K)))
        

if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test_example_1(self):
        self.assertFalse(snapper_chain(1, 0))
        
    def test_example_2(self):
        self.assertTrue(snapper_chain(1, 1))
    
    def test_example_3(self):
        self.assertFalse(snapper_chain(4, 0))
        
    def test_example_4(self):
        self.assertTrue(snapper_chain(4, 47))