from functools import reduce
def solve(num, digits):
    n = len(digits)
    ans = [0] * n
    for i in range(n):
        ans[i:] = [digits[i]]*(n-i)
        v = reduce(lambda x,y: x*10+y, ans)
        if v > num:
            ans[i] = digits[i]-1
            ans[i+1:] = [9]*(n-i-1)
            break
    return reduce(lambda x,y: x*10+y, ans)

for case in range(1, int(input())+1):
    S = input()
    answer = solve(int(S), list(map(int, S)))
    print('Case #{}: {}'.format(case, answer))
