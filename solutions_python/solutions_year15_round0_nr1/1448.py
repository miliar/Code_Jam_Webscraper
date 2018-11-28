T = int(input())

for i in range(T):
    lp = list(map(int, list(input().split()[1])))
    s = 0
    c_st = 0
    for shy, n in enumerate(lp):
        if n > 0 and shy > c_st:
            s += shy - c_st
            c_st += shy - c_st
        c_st += n
    print('Case #{}: {}'.format(i + 1, s))
