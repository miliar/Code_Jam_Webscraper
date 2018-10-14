for sadsf in range(int(input())):
    L = list(map(int, input()))
    n = len(L)
    lastest = n
    for i in range(n-1, 0, -1):
        if L[i] < L[i-1]:
            lastest = i
            L[i-1] -= 1
    for i in range(lastest, n):
        L[i] = 9
    num = int(''.join(map(str, L)))
    print('Case #{}: {}'.format(sadsf + 1, num))
            
