def get_y(intervals):
    t_0 = min(intervals)
    deltas = [t - t_0 for t in intervals if t != t_0]
    
    d = 0
    for dt in deltas:
        d = get_gcd(d, dt)
    
    return (-t_0) % d

def get_gcd(m, n):
    while m and n:
        if m < n: m,n = n,m
        m = m % n
    return m or n
    

def main(input, output):
    case_count = int(input.readline())
    for i in xrange(case_count):
        intervals = map(int, input.readline().strip().split())
        N = intervals[0]
        intervals = intervals[1:]
        assert N == len(intervals)
        
        y = get_y(intervals)
        print >> output, 'Case #%d: %s' % (i+1, y)
        
    
if __name__ == '__main__':
    import sys
    main(open(sys.argv[1]), sys.stdout)