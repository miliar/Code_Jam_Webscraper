def solve(p):
    
    pos = str(p)
    total = 0
    friends = 0
    
    for n in range(len(pos)):
        num = int(pos[n])
        if total >= n:
            total += num
        elif total < n:
            diff = n - total
            friends += diff
            total += diff + num
    
    return(friends)

with open('ova_lg.txt', 'w') as target:   
    with open('A-large.in') as test:
        total_cases = int(test.readline())
        case = 1
        while case <= total_cases:
            s, p = test.readline().strip().split(' ')
            target.write('Case #%d: %d' %(case, solve(p)) + '\n')
            case += 1