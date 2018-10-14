def solve_test_case(C, F, X):
    if (X <= C):
        return X/2.0
    
    last_time = X/2.0
    
    i = 1
    while (True):
        next_time = last_time - X/(2.0 + (i-1)*F) + C/((i-1)*F + 2) + X/(i*F + 2)
        if (next_time > last_time):
            return last_time
        else:
            last_time = next_time
            i += 1
            
number_of_test_cases = int(raw_input())
for i in range(1, number_of_test_cases+1):
    input = raw_input().split(' ')
    C, F, X = [float(l) for l in input]
    print 'Case #%d: %.7f' % (i, solve_test_case(C,F,X))