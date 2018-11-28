def occupy(n):
    f = (n-1) // 2
    return [f, n-1-f]

cases = int(input())
for case in range(1, cases+1):
    n, p = map(int, input().split())
    s = [n]
    for i in range(p):
        if not s:
            new_s = [0, 0]
            break
        new_s = occupy(s.pop())
        c_new_s = [c for c in new_s if c not in [0, 1]]
        s = sorted(c_new_s + s)
    print('Case #{}: {} {}'.format(case, max(new_s), min(new_s)))
