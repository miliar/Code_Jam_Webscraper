import sys

def calc(t):
    ro, ri = t+1, t
    return (ro*ro - ri*ri)

def solve(r, t):
    use = calc(r)
#    print r, use, t
    cnt = 0;
    while use <= t:
        cnt += 1
        r += 2
        t -= use
        use = calc(r)
#        print r, use, t
    return cnt
        

def main():
    data = sys.stdin.readlines()
    num = int(data[0])
    index = 1
    for i in range(1, num+1):
        l = [float(m) for m in data[i].split()]
        r,t = l[0], l[1]
        res = solve(r, t)
        print 'Case #%d:' % i, res

main()
