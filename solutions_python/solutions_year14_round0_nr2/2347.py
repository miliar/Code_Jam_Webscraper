def solve(C, F, X):
    time_taken = X / 2
    prod = 2
    time = 0
    
    while True:
        time = time + C / prod
        prod = prod + F
        if time + X / prod < time_taken:
            time_taken = time + X / prod
        else:
            break
            
    return format(time_taken, '.7f')

def read_input():
    C, F, X = map(float, raw_input().split(' '))
    return C, F, X

for case_n in range(1, int(raw_input()) + 1):
	print 'Case #%s: %s' % (case_n, solve(*read_input()))