import sys
import math

def pal(num):
    nn = int(num)
    if nn-num != 0: return False
    
    s = str(nn)
    ss = s[::-1]
    n = int(ss)
    if nn == n: return True
    return False

def main():
    data = sys.stdin.readlines()
    loop = int(data[0].strip())
    index = 1
    for i in range(1, loop+1):
        ll = data[index].split()
        index+=1
        s, e = int(ll[0]), int(ll[1])
        cnt = 0
        for m in range(s, e+1):
            ms = math.sqrt(m)
            if pal(m) and pal(ms):
                cnt += 1
        print 'Case #%d: %d' % (i, cnt)
    
main()
