import fractions
import math

def solve(t):
    p, q = [int(x) for x in raw_input().strip().split('/')]
    x = fractions.gcd(p, q)
    p, q = (p / x), (q / x)
    log_q = int(math.log(q, 2))
    if 2 ** log_q != q or log_q > 40:
        print 'Case #%d: impossible' % (t,)
    else:
        result = math.ceil(math.log(float(q) / float(p), 2))
        print 'Case #%d: %d' % (t, int(result))
    
def main():
    t = int(raw_input().strip())
    for i in xrange(1, t + 1):
        solve(i)

if __name__ == '__main__':
    main()
