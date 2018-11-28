for T in range(int(input())):
    arr, K = [x for x in input().strip().split(' ')]
    K = int(K)
    arr = [True if x=='+' else False for x in arr]
    #print(arr)
    L = len(arr)
    F = 0
    for i, a in enumerate(arr):
        if not a and L-K >= i:
            arr[i:i+K] = [not j for j in arr[i:i+K]]

            # print(arr)
            F += 1

    if False in arr:
        print('Case #%d: %s' % (T+1, 'IMPOSSIBLE'))
    else:
        print('Case #%d: %s' % (T+1, str(F)))
