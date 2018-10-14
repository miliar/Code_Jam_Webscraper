def determine(s, k):
    res = 0
    lst = list(s)
    for i in range(len(lst)):
        if lst[i] == '-':
            res += 1
            for j in range(k):
                if i + j >= len(lst):
                    return 'IMPOSSIBLE'
                else:
                    if lst[i + j] == '+':
                        lst[i + j] = '-'
                    else:
                        lst[i + j] = '+'
    return res

T = int(input())
for i in range(T):
    s, k = input().split()
    k = int(k)
    print('Case #' + str(i + 1) + ': ' +  str(determine(s, k)))
