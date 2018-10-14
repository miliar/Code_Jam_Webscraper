#!/usr/bin/env python
import sys


def read_n(a):
    n = int(a[0])
    return a[1:n+1], a[n+1:]


def solve():
    global cc, dd
    data = sys.stdin.readline().split()
    cc, data = read_n(data)
    dd, data = read_n(data)
    assert len(data)==2
    nn = data[1]
    ret = []
    for ch in nn:
        ret.append(ch)
        while combine(ret):
            pass
        # Check for "oppose".
        for a,b in dd:
            if (a in ret) and (b in ret):
                ret = []
    return ret

    
def combine(ret):
    if len(ret)<2:
        return
    for a,b,c in cc:
        if (a==ret[-2] and b==ret[-1]) or (a==ret[-1] and b==ret[-2]):
            ret.pop()
            ret.pop()
            ret.append(c)
            return True
    return False
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}: [{}]".format(t+1, ', '.join(solve()))

