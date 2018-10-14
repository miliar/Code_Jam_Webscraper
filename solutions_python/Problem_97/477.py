
def countRecyc(n, b):

    cnt = 0
    
    pwr = 1
    while pwr <= n: pwr *= 10
    pwr /= 10

    m = n

    while True:
        r = m % 10
        m = pwr*r + m / 10
        if m == n: break
        if n < m <= b:
            cnt += 1

    return cnt


def main():
    t = int( raw_input() )
    for i in range(t):
        [a, b] = raw_input().split()
        a = int(a)
        b = int(b)
        cnt = 0
        for n in xrange(a, b):
            cnt += countRecyc(n, b)
        print 'Case #%s: %s' % (i+1, cnt)


if __name__ == '__main__':
    main()
