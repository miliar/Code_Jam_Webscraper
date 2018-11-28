'''
Created on May 7, 2010

@author: patnaik
'''

import sys

vmap = {True:1, False:0}
smap = {True:'ON', False:'OFF'}

def print_soln(bitvect):
    #print ' '.join(map(lambda x: str(vmap[x]), bitvect))
    val = 0
    for i in bitvect:
        val = val * 2 + vmap[i]
    print val

def findsol(n,k):
    flag = False
    bitvect = [False for _ in xrange(n)]
    for i in xrange(k):
        for j in xrange(n):
            if (j == 0 or bitvect[j-1] == False):
                #toggle
                bitvect[j] = not bitvect[j]
            else:
                break
        #print_soln(bitvect)
        if not any(bitvect): 
            k = k % (i + 1)
            flag = True
            #print 'Found periodicity at ', (i+1), 'remaining = ', k
            break
    
    # Solve smaller
    if flag:
        for i in xrange(k):
            for j in xrange(n):
                if (j == 0 or bitvect[j-1] == False):
                    #toggle
                    bitvect[j] = not bitvect[j]
                else:
                    break
            #print_soln(bitvect)

    return smap[all(bitvect)]

if __name__ == '__main__':
    
    line = sys.stdin.readline()
    count = int(line)
    
    for i in xrange(count):
        line = sys.stdin.readline()
        parts = line.split()
        n, k = int(parts[0]), int(parts[1])
        print 'Case #%d: %s' % (i+1, findsol(n, k))
    
