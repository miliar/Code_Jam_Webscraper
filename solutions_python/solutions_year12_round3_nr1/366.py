from sys import stdin
import numpy as np

def resta(x):
    return int(x) - 1


def find(n,m,dic,src,si):
##    print '----------', dic, src, si, '>>',m[si]
    found = False
    for i in xrange(len(src)):
        dic.setdefault(src[i],[])
        if(si in dic[src[i]]):
##            print 'Found',src[i], si
            return True
        else:
            dic[src[i]].append(si)
##            print '+++',dic, src
   
    for j in xrange(len(m[si])):
        found = found or find(n,m,dic,src+[si], m[si][j])
    return found

count = 1
num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    n = int(stdin.readline().strip())
##    m = [[0 for i in xrange(n)] for j in xrange(n)]
    m = []

    for i in xrange(n):
        mt = (map(resta,stdin.readline().strip().split(' ')))
        mt.pop(0)
        m.append(mt)
##    print m

    found = False
    for i in xrange(n):
        dic = {}        
        found = found or find(n,m,dic,[],i)
        if found: break 
    
    res = 'Yes' if found else 'No'
    print "Case #" + str(case_index) + ": " + str(res)
##    count += 1
##    if count == 3: break



