def consume(maxcake, cakes):
    time = 0
    for cake in cakes:
        if cake <= maxcake:
            return time + maxcake
        time += (cake + maxcake - 1) / maxcake - 1
    return time + maxcake

def solve(nonempty, cakes):
    cakes.sort(reverse=True)
    maxcake = cakes[0]
    if maxcake <= 2:
        return maxcake
    ans = 1000 * 1000
    for i in xrange(2, maxcake + 1):
        time = consume(i, cakes)
        if time < ans:
            ans = time
    return ans

def main():
    T = input()
    for i in xrange(1, T + 1):
        nonempty = input()
        cakes = map(int, raw_input().strip().split())
        print 'Case #{0}: {1}'.format(i, solve(nonempty, cakes))

if __name__ == '__main__':
    main()
