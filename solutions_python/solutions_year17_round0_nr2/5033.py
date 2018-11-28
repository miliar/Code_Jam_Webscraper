for case in range(1, int(input()) + 1):
    for n in range(1, int(input()) + 1):
        n_li = list(str(n))
        if n_li == sorted(n_li):
            tidy = ''.join(n_li)
    print("Case #" + str(case) + ': ' + tidy)
