#!/usr/bin/python
import sys
import unittest
import math
Debug=False
sys.setrecursionlimit(100000000)

def d(Str):
    if Debug: print Str

def flip(S,K,pos,count):
    d("%s:pos:%dcnt:%d" % ("".join(S),pos,count))
    if not has_garbage(len(S),S):
        return count
    elif pos > len(S) - K :
        return "IMPOSSIBLE"

    NewS = flip_range(pos, pos+K-1, S)
    res2 = flip(NewS, K, pos+1, count+1)
    best_res1 = "IMPOSSIBLE"
    for i in range(pos, len(S) - K):
        res1 = flip(S,K,i+1,count)
        if res1 != "IMPOSSIBLE":
            if best_res1 == "IMPOSSIBLE":
                best_res1 = res1
            elif res1 < best_res1:
                best_res1 = res1
    if res2 == "IMPOSSIBLE" and best_res1 == "IMPOSSIBLE":
        return "IMPOSSIBLE"
    if res2 != "IMPOSSIBLE" and best_res1 != "IMPOSSIBLE":
        return min(res2, best_res1)
    elif res2 != "IMPOSSIBLE":
        return res2
    elif best_res1 != "IMPOSSIBLE":
        return best_res1



def run(S,K):
    return flip(S,K,0,0)

def flip_range(start, end, S):
    return "".join(do_flip_range(start, end, S))

def has_garbage(end, S):
    if len(S) == 0:
        return False
    if type(S) == str:
        S = list(S)
    if '-' in S[0:end]:
        return True
    else:
        return False


def do_flip_range(start, end, S):
    if type(S) == str:
        S = list(S)
    for n in range(start,end+1):
        if S[n] == '-':
            S[n] = '+'
        else:
            S[n] = '-'
    return S

class TestMe(unittest.TestCase):
    def test_flip_range(self):
        self.assertEqual("-",flip_range(0,0,"+"))
        self.assertEqual("--",flip_range(0,0,"+-"))
        self.assertEqual("-+",flip_range(0,1,"+-"))
        self.assertEqual("+++",flip_range(0,2,"---"))
    def test_has_garbage(self):
        self.assertTrue(has_garbage(1,"---"))
        self.assertFalse(has_garbage(4,"++++"))
        self.assertTrue(has_garbage(4,"+++-"))
        self.assertFalse(has_garbage(3,"+++-"))

if __name__ == '__main__':
    filename=sys.argv[1]
    f = open(filename)
    loops = int(f.readline())
    for i in range(0,loops):
        d("Testcase %d" % (i+1))
        [S, K] = f.readline().split(' ')
        K=int(K)
        d( "K is %d S is %s" % (K, S))
        print "Case #%d: %s" % (i+1, str(run(S,K)))
