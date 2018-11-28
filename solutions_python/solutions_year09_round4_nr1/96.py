def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def main():
    T = int(raw_input())
    for case in xrange(1, T + 1):
        N = int(raw_input())
        rows = tuple(len(raw_input().rstrip('0')) for _ in xrange(N))

        @memoize
        def solve(rows):
            if all(i <= j + 1 for j, i in enumerate(rows)):
                return 0
            min_cost = 1000000000
            for i in xrange(len(rows) - 1):
                if rows[i] > rows[i + 1]:
                    min_cost = min(min_cost, 1 + solve(rows[:i] + rows[i + 1:i + 2] + rows[i:i + 1] + rows[i + 2:]))
            return min_cost
            
        print 'Case #%d: %d' % (case, solve(rows))

if __name__ == '__main__':
    main()
