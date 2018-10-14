def read_case(line):
    return int(line)

def read_input(path):
    f = open(path, 'r')
    g = open(path + '_res.txt', 'w')
    T = int(f.readline())
    for i in xrange(T):
        line = f.readline()
        g.write('Case #%d: ' % (i+1))
        n = read_case(line)
        g.write(str(solve(n)))
        g.write('\n')
    g.close()
    f.close()

def first_untidy(n):
    res = 0
    while n > 0:
        if n%10 < (n/10)%10:
            return res
        res += 1
        n /= 10
    return -1


def is_units_tidy(n):
    u = n % 10
    while n > 0:
        n /= 10
        if n % 10 > u:
            return False
    return True
  
def solve_after_first(n):
    if n < 10:
        return n
    if not is_units_tidy(n):
        n -= n % 10 + 1
    return solve_after_first(n/10)*10 + n%10

def solve(n):
    k = first_untidy(n)
    if k == -1:
        return n
    n -= n % 10**(k+1) + 1
    return solve_after_first(n)


read_input('B-small-attempt1.in')
    
