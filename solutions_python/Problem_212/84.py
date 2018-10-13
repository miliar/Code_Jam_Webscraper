def solve2(data):
    odd = [x for x in data if x % 2]
    even = [x for x in data if x % 2 == 0]
    return len(even) + (len(odd) + 1) // 2

def solve3(data):
    mod0 = [x for x in data if x % 3 == 0]
    mod1 = [x for x in data if x % 3 == 1]
    mod2 = [x for x in data if x % 3 == 2]
    ans = len(mod0)
    ans += min(len(mod1), len(mod2))
    ans += (abs(len(mod1) - len(mod2)) + 2) // 3
    return ans

def solve4(data):
    mod0 = [x for x in data if x % 4 == 0]
    mod1 = [x for x in data if x % 4 == 1]
    mod2 = [x for x in data if x % 4 == 2]
    mod3 = [x for x in data if x % 4 == 3]
    ans = len(mod0)
    ans += len(mod2) // 2
    ans += min(len(mod1), len(mod3))
    if len(mod2) % 2 and len(mod1) - len(mod3) >= 2:
        ans += 1
        mod1.pop()
        mod1.pop()
        mod2.pop()
    ans += (len(mod2) + 3) // 4
    ans += (abs(len(mod1) - len(mod3)) + 3) // 4
    return ans

def solve(p, m):
    return [solve2, solve3, solve4][p - 2](m)

for i in range(1, int(input()) + 1):
    print('Case #', i, ': ', solve(int(input().split()[1]), list(map(int, input().split()))), sep='')

