T = int(input())
for test_case in range(1, T+1):
    S, K = input().split()
    K = int(K)
    count = 0
    while '-' in S[:-(K-1)]:
        index = S.find('-')
        sub = S[index:index+K]
        sub = sub.replace('-', '=')
        sub = sub.replace('+', '-')
        sub = sub.replace('=', '+')
        S = S[:index]+sub+S[index+K:]
        count += 1
    if '-' in S:
        print("Case #{}: IMPOSSIBLE".format(test_case))
    else:
        print("Case #{}: {}".format(test_case, count))
