'''
Created on May 6, 2011

@author: ola
'''
import math

def find(olist):
    oc = 1
    bc = 1
    ol = 0
    bl = 0
    tm = 0
    #print "data = ",olist
    for tup in olist:
        if tup[0] == "O":
            tomove = int(math.fabs(oc-tup[1]))
            if tm-ol > tomove:
                tomove = 0
            else:
                tomove -= (tm-ol)
            tm +=  tomove + 1
            oc = tup[1]
            ol = tm
        else:
            tomove = int(math.fabs(bc-tup[1]))
            if tm-bl > tomove:
                tomove = 0
            else:
                tomove -= (tm-bl)
            tm +=  tomove + 1
            bc = tup[1]
            bl = tm
        #print "doing",tup,tm,oc,bc
    return tm

def solve(n):
    olist = []
    data = raw_input().split()
    #print "read",data
    x = int(data[0])
    for x in xrange(0,2*x,2):
        hall = data[x+1]
        but = int(data[x+2])
        olist.append((hall,but))
    print "Case #%d: %d" % (n,find(olist))

def main():
    t = int(raw_input())
    for x in xrange(t):
        solve(x+1)

if __name__ == "__main__":
    main()