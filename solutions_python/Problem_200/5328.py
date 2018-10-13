import sys

def check(t):
    # 1489
    s = str(t)
    m = int(s[0])
    for c in s[1:]:
        if int(c) >= m:
            m = int(c)
        else:
            return False
    return True

def process(N):
    num = long(N)
    while num > 0:
        s = str(num)
        m = int(s[0])
        breaking = True
        for c in s[1:]:
            if int(c) >= m:
                m = int(c)
            else:
                breaking = False
                break
        if breaking:
            return num
        num -=1


if __name__ == '__main__':
    fp = open(sys.argv[1], 'r')
    T = int(fp.readline().strip())
    for case in range(1, T+1):
        N = fp.readline().strip()
        out = process(N)
        print "Case #%s: %s" % (case, out)
