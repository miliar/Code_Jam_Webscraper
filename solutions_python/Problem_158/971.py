def solve(X, R, C):

    if ((R * C) % X) != 0:
        return 'RICHARD'
    if X == 3:
        if R == 1 or C == 1:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    elif X == 4:
        if R >= 3 and C >= 3:
            return 'GABRIEL'
        else:
            return 'RICHARD'
            
    return 'GABRIEL'
    

with open('d_sm.txt', 'w') as target:
    with open('D-small-attempt1.in') as test:
        total_cases = int(test.readline())
        case = 1
        while case <= total_cases:
            X, R, C = (int(x) for x in test.readline().strip().split(' '))
            target.write('Case #%d: %s' %(case, solve(X, R, C)) + '\n')
            case += 1