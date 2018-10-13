def tidy(x):
    s = list(str(x))
    return s == sorted(s)

N = int(input())
for n in range(1, N+1):
    x = int(input() + '9')
    s = [int(c) for c in str(x)]
    while True:
        #print(s)
        ok = True
        i = 0
        while i < len(s) - 1:
            if s[i] > s[i+1]:
                ok = False
                break
            i += 1
        if ok:
            break
        #print(s, x, ok, i)
        s[i], s[i+1] = s[i]-1, 9
        i += 1
        while i < len(s):
            s[i] = 9
            i += 1
    ans = int(''.join([str(c) for c in s[:-1]]))
    print('Case #{}: {}'.format(n, ans))

