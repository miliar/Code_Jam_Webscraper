#!/usr/bin/env python
import sys
def Snap(N, k):
    e = 2**N
    kmod = (k % (e)) + 1
    return int(kmod == e)
def main():
    it = iter(sys.stdin)
    T = int(next(it))
    out = ['OFF', 'ON']
    for x in range(1, T+1):
        N, k = map(int, next(it).split())
        y = Snap(N, k)
        print "Case #%d: %s" %(x, out[y])
            

if __name__=='__main__':
    main()
