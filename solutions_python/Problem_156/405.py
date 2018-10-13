for j in range(int(raw_input())):
 
    I = int(raw_input())
 
    A = list(map(int, raw_input().split(" ")))
 
    result = max(A)
 
    Z = 2
    while Z < result:
        result = min(result, sum([(x - 1) // Z for x in A]) + Z)
        Z += 1
 
    print 'Case #%d: %s' % (j + 1, result)