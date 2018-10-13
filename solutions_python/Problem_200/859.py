def f(s):
    l = list(map(int,s))
    n = len(l)
    a = l[-1]
    for i in reversed(range(n-1)):
        if l[i] > a:
            l[i] -= 1
            l[i+1:] = [9]*(n-i-1)
        a = l[i]
    return int(''.join(map(str, l)))
for _ in range(int(input())):
    print('Case #%s: %s' % (_+1, f(input())))