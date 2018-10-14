def read_int():
    return int(raw_input())


def read_int_list():
    return [int(x) for x in raw_input().split()]

def swap(val):
    if val == '-':
        return '+'
    return '-'

def solve():
    cake, K = raw_input().strip().split(' ', 1)
    K = int(K)
    cake = list(cake)
    cnt = 0
    for i in xrange(0, len(cake) - K + 1):
        if cake[i] == '-':
            for j in xrange(K):
                cake[i + j] = swap(cake[i + j])
            cnt += 1
    for x in cake:
        if x == '-':
            return 'IMPOSSIBLE'
    return cnt

def main():
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())

if __name__ == '__main__':
    main()
