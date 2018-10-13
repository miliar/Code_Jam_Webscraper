
for case in range(int(input())):
    D = int(input())
    P = [int(x) for x in raw_input().split(' ')]
    result = max(P)
    count = 2 
    while count <result:
        result = min(result,sum([(x - 1 ) // count for x in P]) + count)    
        count += 1
    print('Case #%d: %s' % (case + 1 ,result))
