def solve(cakes, N):
    left = []
    count = 0
    to_print = []
    for cake in cakes:
        if (int(bool(cake == '-')) + len(left)) % 2:
            left.append(N)
            count += 1
        left = map(lambda x: x - 1, left)
        left = filter(lambda x: x != 0, left)
    if len(left):
        return 'IMPOSSIBLE'
    else:
        return count

def main():
    T = input()
    for i in xrange(1, T + 1):
        cakes, N = raw_input().strip().split()
        N = int(N)
        print 'Case #{0}: {1}'.format(i, solve(cakes, N))

if __name__ == '__main__':
    main()
