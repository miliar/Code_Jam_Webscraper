'''
Created on May 6, 2011

@author: conan
'''
from Tool import *
from itertools import *
import itertools

def patrick(lst):
    s = 0
    for n in lst:
        s = s ^ n
    return s
        
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))        
        
def solve(lst):
    lst = sorted(lst)
    if patrick(lst) != 0:
        return 'NO'
    else:
        for p in powerset(lst):
            if len(p) > 0 and len(p) < len(lst):
                remain = diff(p, lst)
                if patrick(p) == patrick(remain):
#                    print p, remain
                    return sum(remain)

def diff(st1, st2):
    rv = []
    i = 0
    j = 0
    while i < len(st1):
        if st1[i] != st2[j]:
            rv += [st2[j]]
            j += 1
        else:
            i += 1
            j += 1
    rv += st2[j:]
    return rv
               
def output(f):
    f = open(f)
    w = open('out.txt', 'w')
    f.readline()
    lines = []
    counter = 1
    for line in f:
        lines.append(line)
    for i in range(1, len(lines), 2):
        candies = map(int, lines[i].split())
        r = 'Case #{}: {}\n'.format(counter, solve(candies))
        print r
        w.write(r)
        counter += 1
        

    f.close()
    w.close()
    
if __name__ == '__main__':
#    print diff([5], [5, 5])
    output('c-large.in')
#    for p in powerset([5, 5]):
#        print p
#    print solve([5, 5])
