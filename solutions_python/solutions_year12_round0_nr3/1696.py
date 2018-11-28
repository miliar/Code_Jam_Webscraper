'''
Created on 14.04.2012

@author: stade
'''
import time

def arePerms(a,b):
    a_str = str(a)
    b_str = str(b)
    return sorted(a_str) == sorted(b_str)

def recycledNumbers(a, b):
    cnt = 0
    for i in range(a,b):
        for j in range (i+1,b+1):
            if arePerms(i,j):
                if areRecycled(i,j):
                    cnt += 1
    print cnt
    return cnt

def areRecycled(a,b):
    for i in xrange(1,len(str(a))):
        suffix = a%10**(len(str(a))-i)
        prefix = a/10**(len(str(a))-i)
        n = suffix*10**i+prefix
        if n == b:
            return True
    return False
          
def sol():
    f = open("/Users/stade/Downloads/C-small-attempt0.in", "r")
    f.next() # skip firt line
    w = open("/Users/stade/Downloads/output.txt", "w")
    cnt = 1
    for line in f:
        a = int(line.split(" ")[0])
        b = int(line.split(" ")[1])
        sol = recycledNumbers(a, b)
        print "Case #%d: %s" %(cnt, sol)
        w.write("Case #%d: %s\n" %(cnt, sol))
        cnt += 1
    w.close()


if __name__ == '__main__':
    t0 = time.clock()
    sol()
    t1 = time.clock()
    print "%d s"  %(t1-t0)