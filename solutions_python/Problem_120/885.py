'''
Created on Apr 27, 2013

@author: santosh
'''

if __name__ == '__main__':
    T = int(raw_input())
    for t in xrange(T):
        inp = raw_input().split()
        (r, p) = (int(inp[0]), int(inp[1]))
        sm = 0
        i = r
        while sm <= p:
            sm = sm + 2 * i + 1
            i += 2
        print "Case #%d: %d"%(t+1,(i-1-r)/2)
