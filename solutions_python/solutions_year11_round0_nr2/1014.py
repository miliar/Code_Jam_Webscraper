#!/usr/bin/env python
'''
Magicka
'''

import sys
verbose = False

def read_input(fname):
    cases = []
    with open(fname) as f:
        case_num = int(f.next().strip())
        for line in f:
            cases.append(Case(line.strip()))
    return cases
    
class Case(object):
    def __init__(self,line):
        self.combine_pairs = {}
        self.opposed_pairs = {}
        self.invoke = []
        
        self.cp = []
        self.op = []
        
        tokens = line.split()
        
        c = int(tokens[0])
        tokens = tokens[1:]
        
        for i in xrange(c):
            triad = tokens[0]
            tokens = tokens[1:]
            self.cp.append(triad)
            
            self.combine_pairs[(triad[0],triad[1])] = triad[2]
            self.combine_pairs[(triad[1],triad[0])] = triad[2]

        d = int(tokens[0])
        tokens = tokens[1:]
        
        for i in xrange(d):
            dpair = tokens[0]
            tokens = tokens[1:]
            self.op.append(dpair)
            
            self.opposed_pairs[dpair[0]] = dpair[1]
            self.opposed_pairs[dpair[1]] = dpair[0]

        n = int(tokens[0])
        
        for el in tokens[1]:
            self.invoke.append(el)

        
    def solve(self):
        _log(str(self.cp))
        _log(str(self.op))
        _log(str(self.invoke))
        _log('------------------------')
        
        last = None
        out = []
        
        t=0
        for cur in self.invoke:
            _log('%4s | [%s] + %s' % (t,', '.join(out), cur))
            if (cur,last) in self.combine_pairs:
                out = out[:-1]
                out.append(self.combine_pairs[(cur,last)])
                last = None
            elif cur in self.opposed_pairs and self.opposed_pairs[cur] in out:
                out = []
                last = None
            else:
                out.append(cur)
                last = cur
            t+=1

        _log('%4s | [%s]' % (t,', '.join(out)))
            
        return '[%s]' % ', '.join(out)

def _log(s):
    if not verbose:
        return
    sys.stderr.write('%s\n' % s)
    

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[2] == '-v':
        verbose = True
        
    cases = read_input(sys.argv[1])
    
    for num,case in enumerate(cases):
        if verbose:
            sys.stderr.write('------------------------\nCase #%s\n------------------------\n' % (num+1))
        t = case.solve()
        print 'Case #%s: %s' % (num+1,t)
        if verbose:
            sys.stderr.write('Case #%s: %s\n' % (num+1,t))
            sys.stdin.readline()