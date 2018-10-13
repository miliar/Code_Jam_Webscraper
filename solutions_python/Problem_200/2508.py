T = int(input())
for test_case in range(1, T+1):
    M = int(input())
    N = M
    if N < 10:
        print("Case #{}: {}".format(test_case, M))
    else:
        if N == 10:
            print("Case #{}: 9".format(test_case))
        else:
            while N > 9:
                if '0' in str(M):
                    m = str(M)
                    # print(N, M)
                    ind1 = m.rfind('0')
                    ind2 = len(m)-ind1
                    m = m+'0'
                    M -= (M % (10**ind2)) + 1
                    N = M
                    continue
                u = N % 10
                N = N // 10
                v = N % 10
                if v > u:
                    # print(N, M, u, v)
                    M -= 1
                    N = M
                    continue
                else:
                    if N < 10:
                        print("Case #{}: {}".format(test_case, M))
                        break
