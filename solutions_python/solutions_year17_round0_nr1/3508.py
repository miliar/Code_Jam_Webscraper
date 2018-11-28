T = int(input())
for i in range(T):

    temp = input().split()
    S = temp[0]
    K = int(temp[1])
    pancakes = list(S)
    N = 0
    while ''.join(pancakes) != '+' * len(S):
        start = 0
        end = 0
        for k in range(len(pancakes)):
            if pancakes[k] != '+':
                start = k
                end = k + K
                break
        if end > len(pancakes):
            print("Case #{}: IMPOSSIBLE".format(i + 1))
            break
        for k in range(start, end):
            if pancakes[k] == '-':
                pancakes[k] = '+'
            else:
                pancakes[k] = '-'
        N += 1
        # print(pancakes)
    else:
        print("Case #{0}: {1}".format(i + 1, N))
