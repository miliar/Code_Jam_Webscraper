#!/usr/bin/env python
import sys
import time
import cPickle
import re
import math
import itertools
import numpy as np
import networkx as nx


def DBG(*args, **kw):
    print >> sys.stderr, '  ->' * (kw.get('level',1)), 
    for a in args: print >> sys.stderr, a,
    print >> sys.stderr

def DBGF(func):
    def dfunc(*args, **kw):
        ret = apply(func,args, kw)
        DBG("%s(%s) -> %s" % (func.__name__, ', '.join(map(str,args) + map(lambda k,v: str(k)+"="+str(v), kw.items())), ret))
        return ret
    return dfunc

class ParsingMixIn:
    def ReadCase(self):
        R, C = self.ReadInts()
        board = []
        for i in range(R):
            board.append(self.NextLine())
        return R, C, board

    def NextLine(self):
        return next(self.IN).strip()

    def ReadInt(self, base = 10):
        return long(self.NextLine(),base)

    def ReadInts(self, sep = ' ', base = 10):
        return map(lambda x:long(x,base),self.NextLine().split(sep))

    def ParseTuple(self, tp):
        ret0 = re.split(r'\s+',self.NextLine())
        assert len(ret0) == len(tp)
        return tuple( (( f(i) for f,i in itertools.izip(tp, ret0) )) )

class SolvingMixIn:
    @DBGF
    def SolveCase(self, case):
        R, C, board = case
        ret = 0
        
        for i in range(R): # check each row
            for j in range(C): # check from left to right
                a = board[i][j]
                if a != '.':
                    # check if this is an impossible point
                    if len(board[i].strip('.')) == 1:
                        if sum( (( s[j]!='.' for s in board )) ) == 1:
                            return "IMPOSSIBLE"
                        
                    if a == '<': ret += 1
                    break
            for j in range(C-1,-1,-1):
                a = board[i][j]
                if a != '.':
                    if a == '>': ret += 1
                    break
        
        for j in range(C): # check each column
            for i in range(R): # check top to bottom
                a = board[i][j]
                if a != '.':
                    if a == '^': ret += 1
                    break
            for i in range(R-1,-1,-1):
                a = board[i][j]
                if a != '.':
                    if a == 'v': ret += 1
                    break

        return ret 

class WritingMixIn:
    def WriteCase(self,n_case,sol):
        outstr =  "Case #%d: %s" % (n_case, sol)
        if self.OUTFN: DBG(outstr)
        print >> self.OUT, outstr

precalc_table = {} # maps precalc key to precalc data
def PreCalc(key):
    """ """
    if key not in precalc_table:
        precalc_table[key] = PreCalcInst(key)
    return precalc_table[key]

class PreCalcInst(object):
    def __init__(self, key):
        self.key = key

    def precalc(self):
        pass

    def load_or_dump(self):
        A, B, C = self.key
        f = None
        fn = 'precalc-%s.pkl' % '-'.join( map(str, self.key) )
        try:
            f = open(fn, 'rb')
            self.product_prob = cPickle.load(f)
        except IOError:
            self.precalc()
            f = open(fn, 'wb')
            cPickle.dump(self.product_prob, f)

class Boiler(ParsingMixIn,SolvingMixIn,WritingMixIn):
    def main(self):
        IN = INFN = None
        OUT = OUTFN = None
        if len(sys.argv)>1:
            INFN = sys.argv.pop()
            IN = open(INFN,'rt')
            OUTFN = INFN.rstrip('.in')+'.out-'+time.strftime('%Y-%m-%d_%H-%M-%S')+'.out'
            OUT = open(OUTFN,'wt')
        else:
            IN = sys.stdin
            OUT = sys.stdout

        self.IN, self.INFN = IN, INFN
        self.OUT, self.OUTFN = OUT, OUTFN
        self.loop()

    def loop(self):
        T = long(self.IN.readline())
        for cas in range(T):
            case = self.ReadCase()
            sol = self.SolveCase(case)
            self.WriteCase(cas+1,sol)

if __name__ == '__main__':
    Boiler().main()
