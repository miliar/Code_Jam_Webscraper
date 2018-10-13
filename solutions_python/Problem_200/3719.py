def compute(s):
    c = s
    zero = c.index('0') if '0' in c else -1
    while(zero > -1):
        c[zero-1] = str(int(c[zero-1]) -1)
        c = c[:zero] + list(len(c[zero:]) * '9')
        if c[0] == '0':
            c = c[1:]
        zero = c.index('0') if '0' in c else -1

    restart = True
    while(restart):
        restart = False
        for i, val in enumerate(c):
            if (i + 1) < len(c):
                if val > c[i+1]:
                    c[i] = str(int(val) - 1)
                    c = c[:i+1] + list(len(c[i+1:]) * '9')
                    restart = True
                    break

    return("".join(c).lstrip('0'))


T = int(input())


for case in range(1, T + 1):
    n = input().strip()
    h = compute(list(n))
    print("Case #{}: {}".format(case, h))
