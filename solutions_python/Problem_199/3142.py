#r = raw_input
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
    s, k = r().split()
    k = int(k)
    s = list(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == '-':
            if i + k > len(s):
                return -1
            for j in range(i, i + k):
                s[j] = '+' if s[j] == '-' else '-'
            cnt += 1
    return cnt

if __name__ == '__main__':
    precompute()

    T = int(r())
    for t in range(1, T + 1):
        ans = solve_case()
        print('Case #%d: ' % t, end='')
        if ans == -1:
            print('IMPOSSIBLE')
        else:
            print(ans)
