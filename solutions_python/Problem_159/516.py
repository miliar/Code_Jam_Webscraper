def solve_1(n):
    
    t_1 = 0
    
    for x in range(1, len(n)):
        if n[x] < n[x-1]:
            t_1 += n[x-1] - n[x]
    
    return t_1
            
def solve_2(n):
    
    rate = 0
    t_2 = 0
    
    for y in range(1, len(n)):
        t_r = (n[y-1] - n[y])
        if t_r > rate:
            rate = t_r
        
    for z in range(0, len(n) -1):
        if n[z] - rate < 0:
            t_2 += n[z]
        else:
            t_2 += rate
            
    return t_2

with open('a_lg.txt', 'w') as target:
    with open('A-large.in') as test:
        total_cases = int(test.readline())
        case = 1
        while case <= total_cases:
            d = test.readline().strip()
            n = list(int(x) for x in test.readline().strip().split(' '))
            target.write('Case #%d: %d %d' %(case, solve_1(n), solve_2(n)) + '\n')
            case += 1