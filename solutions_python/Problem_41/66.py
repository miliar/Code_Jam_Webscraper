#import numpy
#import scipy
import sys
import csv
#from numpy import zeros
#from numpy import size

def __main__():
    input = sys.argv[1]

    r = csv.reader(open(input),delimiter=' ',quoting=csv.QUOTE_NONE)
    t=int(r.next()[0])
    for i in range(0,t):
        [n] = r.next()
#        print n
        next = solve('0'+n)
        if next[0]=='0':
            next = next[1:]
        print "Case #"+str(i+1)+": "+next

def solve(n):
    if (len(n)==1):
        return(n+'0')
    else:
        n_sub = n[1:]
        n_sub_next = solve(n_sub)
#        print n, n_sub_next
        if (len(n_sub_next) == len(n_sub)):
            return(n[0] + n_sub_next)
        else:
            if (n[0] == '0'):
#                print upgrade(n[1:])
                n_next = upgrade(n[1:])
                return(n_next)
            else:
                n_next = reorder(n[0],n[1:]);
                if n_next == n:
                    return(upgrade(n))
                else:
                    return(n_next)

def upgrade(n):
    s = len(n)
    l = split(n)
    count = 0
    while l.count('0')>0:
        l.remove('0')
        count = count + 1
    if len(l)==0:
        return(n)
    l.sort()
    next = l[0]
    for i in range(0, count + 1):
        next = next + '0'
    for i in range(1, len(l)):
        next = next + l[i]
    return(next)
    
def reorder(n0, n1):
    l1 = split(n1)
    best = 'a'; pos = -1
    for i in range(0,len(l1)):
        if l1[i] > n0:
            if l1[i]<best:
                best = l1[i]; pos = i
    if pos==-1:
        return(n0+n1)
    else:
        l1.remove(best)
        l1.append(n0)
        l1.sort()
        result = best
        for i in range(0,len(l1)):
            result = result + l1[i]
        return(result)

def split(n):
    l = []
    for i in range(0,len(n)):
        l.append(n[i])
    return(l)

if __name__ == '__main__': __main__()