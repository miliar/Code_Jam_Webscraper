def solve(levels, data):
    stoodup = 0
    ans = 0
    for j in xrange(levels + 1):
        if stoodup < j:
            ans += j - stoodup
            stoodup = j
        stoodup += int(data[j])
    return ans

def main():
    n = input()
    for i in xrange(1, n + 1):
        line = raw_input()
        levels, data = line.strip().split()
        levels = int(levels)
        print 'Case #{0}: {1}'.format(i, solve(levels, data))

if __name__ == '__main__':
    main()
