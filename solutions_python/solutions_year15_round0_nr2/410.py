from math import ceil

def calc_time(d, ps):
    ps.sort()
    upb = ps[-1]
    ret = upb
    for i in reversed(xrange(1, upb+1)):
        special = 0
        for p in ps:
            if p <= i:
                continue
            special += int(ceil(float(p) / i)) - 1
        ret = min(ret, special + i)
    return ret

def main():
    t = int(raw_input())
    for k in xrange(1, t+1):
        d = int(raw_input())
        ps = map(int, raw_input().split())
        print 'Case #%d: %d' % (k, calc_time(d, ps))

if __name__ == '__main__':
    main()
