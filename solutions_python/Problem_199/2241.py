def crop(s):
    while (len(s) > 0) and (s[0] == '+'):
        s = s[1:]
    while (len(s) > 0) and (s[-1] == '+'):
        s = s[:-1]
    return s

## iters input
cases = int(input())

for case in range(cases):
    ## params input
    s, k = input().split()
    s = list(s)
    k = int(k)

    ## begin
    flips = 0
    s = crop(s)

    while (len(s) >= k):
        for c in range(k):
            if (s[c] == '+'):
                s[c] = '-'
            else:
                s[c] = '+'

        s = crop(s)
        flips += 1

    ## output
    if (len(s) > 0):
        print('Case #' + str(case + 1) + ': IMPOSSIBLE')
    else:
        print('Case #' + str(case + 1) + ':', flips)
