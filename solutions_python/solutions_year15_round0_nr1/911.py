def solve(s):
    clapping = 0
    add = 0
    for i in range(0, len(s)):
        p = int(s[i])
        increase = max(0, i - clapping)
        add += increase
        clapping += increase + p
    
    return add

T = int(input())

for i in range(1, T + 1):
    
    params = input().split()

    print("Case #", i, ": ", solve(params[1]), sep='')


