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
        N = self.ReadInt()
        sentences = [ self.NextLine().split(' ') for i in range(N) ]

        return sentences

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
        sentences = case
        ENG, FR = sentences[:2]
        G = nx.Graph()
        G.add_node('E')
        G.add_node('F')
        G.add_edges_from( (( ('E',w) for w in ENG )) )
        G.add_edges_from( (( ('F',w) for w in FR )) )
        bad = list(set(ENG) & set(FR))
        for b in bad: G.remove_node(b)
        for s in sentences:
            G.add_nodes_from([ n for n in s if n not in bad ])
            for i in range(len(s)):
                if s[i] in bad: continue
                G.add_edges_from( (( (s[i],s[j]) for j in range(i+1,len(s)) if s[j] not in bad )) )
    

        return len(bad) + len(nx.algorithms.connectivity.minimum_node_cut(G,'E','F'))

class WritingMixIn:
    def WriteCase(self,n_case,sol):
        outstr =  "Case #%d: %s" % (n_case, sol)
        if self.OUTFN: DBG(outstr)
        print >> self.OUT, outstr

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
