SET_NAME = 'B-large'

def solve_case(infile):
    events = map(int, infile.readline().split())[1:]
    diffs = map(lambda x: x - events[0], events[1:])
    divisor = gcd_set(diffs)
    time_until = (divisor - (events[1] % divisor)) % divisor
    return time_until

def gcd_set(ints):
    if len(ints) == 1:
        return abs(ints[0])
    else:
        return gcd(gcd_set(ints[0:len(ints)//2]), gcd_set(ints[len(ints)//2:]))
    
def gcd(m, n):
    if m > n:
        return gcd(n, m)
    elif m < 0:
        return gcd(m*-1, n)
    elif m == 0:
        return n
    else:
        return gcd(n % m, m)
    
def main():
    """
    Standard main method for all google code jam problems
    """
    infile = open('%s.in'%(SET_NAME))
    outfile = open('%s.out'%(SET_NAME), 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        print 'Solving case #%d...'%(i+1)
        output = 'Case #%d: %s\n'%(i+1, solve_case(infile))
        print output
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()