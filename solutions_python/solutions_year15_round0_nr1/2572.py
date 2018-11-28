#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Initially, the entire audience is seated. Everyone in the audience has a shyness level. An audience member with shyness level Si will wait until at least Si other audience members have already stood up to clap, and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always stand up and clap immediately, regardless of what anyone else does. For example, an audience member with Si = 2 will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing and clapping.
'''
debug=False
import unittest

class TestStandingOvations(unittest.TestCase):
    def test_Case1(self):
        self.assertEqual(getSolution([1,1,1,1,1]), 0)
    def test_Case2(self):
        self.assertEqual(getSolution([0,9]), 1)
    def test_Case3(self):
        self.assertEqual(getSolution([int(x) for x in '110011']), 2)
    def test_Case4(self):
        self.assertEqual(getSolution([1]), 0)
    def test_Case5(self):
        self.assertEqual(getSolution([3,0,0,1,1]), 0)
    def test_Case6(self):
        self.assertEqual(getSolution([0,0,0,0,1]), 4)

def getSolution(shyness):
    standing=0
    allFriends=0
    for index,numOfPeople in enumerate(shyness):
        friends=index-standing
        if friends > 0:
            standing+=friends
            allFriends+=friends
        standing+=numOfPeople
    return allFriends

if __name__ == "__main__":
    if debug:
        unittest.main()
    else:
        with open('A-large.out','wb') as outputFile:
            with open('A-large.in','rb') as inputFile:
                testcases=int(inputFile.readline())
                for case in xrange(testcases):
                    maxShyness,shynessLevels=inputFile.readline().split()

                    sol = getSolution([int(x) for x in shynessLevels])
                    outputFile.write('Case #%d: %d\n'%(case+1,sol))
