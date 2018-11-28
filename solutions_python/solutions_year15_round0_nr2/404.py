for j in range(int(input())):
 
    I = int(input())
 
    A = list(map(int, input().split()))
 
    result = max(A)
 
    Z = 2
    while Z < result:
        result = min(result, sum([(x - 1) // Z for x in A]) + Z)
        Z += 1
 
    print('Case #%d: %s' % (j + 1, result))