def is_tidy(N):
    if N < 10:
        return True

    next_digit = N % 10
    N /= 10;
    while N > 0:
        digit = N % 10;
        if digit > next_digit:
            return False
        next_digit = digit
        N /= 10
 
    return True

def solve(N):
    while N > 0:
        if is_tidy(N):
            return N
        N -= 1

    return 0

if __name__ == '__main__':
    lines = open('B-small-attempt0.in', 'r').readlines()
    test_cases = int(lines[0])
    for i in xrange(1, len(lines)):
        print 'Case #{0}: {1}'.format(i, solve(int(lines[i])))