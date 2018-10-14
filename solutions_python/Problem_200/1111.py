def solve(n, ptr, und, pre = 0):

    if ptr == 0:
        for i in range(9, und-1, -1):
            if i > n:
                continue
            return pre*10 + i
        return -1

    for i in range(9, und-1, -1):
        if i * 10**ptr > n:
            continue
        ans = solve(n - i*10**ptr, ptr-1, i)
        if ans != -1:
            return pre * 10**(ptr+1) + i * 10**ptr + ans

    return -1


k = int(input())

for case_num in range(1, k+1):
    str_n = input()
    n = int(str_n)
    
    ans = solve(n, len(str_n) - 1, 0)

    print("Case #%d: %d" % (case_num, ans))
