r = input
rr = lambda: map(int, r().split())

# a decorator for memoization
def memoize(fn):
    memo = {}
    def wrapper(*args):
        if args not in memo: memo[args] = fn(*args)
        return memo[args]
    return wrapper

def precompute():
    pass

def solve_case():
    s = r()
    s_int = int(s)
    ans = ''
    if s_int >= int('1' * len(s)):
        ans = ''
        prv = '0'
        for ch in s:
            if ch >= prv:
                ans += ch
                prv = ch
            else:
                while len(ans) >= 2 and ans[-1] == ans[-2]:
                    ans = ans[:-1]
                ans = ans[:-1] + str(int(ans[-1]) - 1)
                ans += '9' * (len(s) - len(ans))
                break
    else:
        ans =  '9' * (len(s) - 1)
    print(ans)


if __name__ == '__main__':
    precompute()

    T = int(r())
    for t in range(1, T + 1):
        print('Case #%d: ' % t, end='')
        solve_case()
