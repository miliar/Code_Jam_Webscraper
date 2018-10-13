
def insert(d, p):
    count = 0
    paths = p.split('/')
    for i in xrange(len(paths)):
        s = '/'.join(paths[:i+1])
        if s and s not in d:
            d[s] = 1
            count += 1
    return count

def solve():
    count = 0
    dirs = {}

    N, M = map(int, raw_input().split(' '))
    for i in xrange(N):
        insert(dirs, raw_input())
    for i in xrange(M):
        count += insert(dirs, raw_input())

    return count

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%s: %s' % (i + 1, solve())

if __name__ == '__main__':
    main()
