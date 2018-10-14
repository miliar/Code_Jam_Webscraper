#!/usr/bin/env python
'''
Candy Splitting
'''

import sys
import itertools

verbose = False

def read_input(fname):
    cases = []
    with open(fname) as f:
        case_num = int(f.next().strip())
        
        i = 0
        while i < case_num:
            c_count = int(f.next())
            cases.append(Case(f.next().strip()))
            i+=1
            
    return cases
    
class Case(object):
    def __init__(self,line):
        tokens = line.split()
        self.candies = [int(x) for x in tokens]
        
    def solve(self):
        _log(str(self.candies))
        _log('------------------------')
        
        piles = self.calc_piles()
        summed_piles = []
        
        for p1,p2 in piles:
                        
            s1 = self.sum(p1)
            s2 = self.sum(p2)
            
            if s1 >= s2:
                summed_piles.append((s1,p1,p2))
            else:
                summed_piles.append((s2,p2,p1))
            
        summed_piles.sort()
        summed_piles.reverse()

        
        for s1,p1,p2 in summed_piles:
            _log('%s | (%s =? %s) | %s %s' % (s1,self.xor(p1),self.xor(p2),p1,p2)) 
            
            if self.xor(p1) == self.xor(p2):
                return s1
        
        return 'NO'
    
    def calc_piles(self):
        size = len(self.candies)-1

        combos = []
        while size > 0:
            for t in itertools.combinations(self.candies,size):
                combos.append(t)
            size -= 1

        top = combos[:(len(combos)/2)]
        bottom = combos[:(-len(combos)/2)-1:-1]
        
        _log('\n'.join([str(x) for x in combos]))
        
        for t,b in zip(top,bottom):
            yield((t,b))

    def sum(self,pile):
        acc = 0
        for p in pile:
            acc += p
        
        return acc
    
    def xor(self,pile):
        acc = 0
        for p in pile:
            acc ^= p
        
        return acc

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
        sys.stderr.write('Case #%s: %s\n' % (num+1,t))
        if verbose:
            sys.stdin.readline()