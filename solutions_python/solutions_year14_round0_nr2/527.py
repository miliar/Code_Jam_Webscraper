def case(c, f, x):
    solns = [x/2]

    acc = 0
    n = 1
    while True:
        acc += c / (2 + (n-1)*f)

        target = x/(2+n*f) + acc
        if target > solns[-1]:
            break
        solns.append(target)
        n += 1

    return solns[-1]

ncases = int(input())
for i in range(ncases):
    c, f, x = map(float, input().split())
    print('Case #%d: %.7f' % (i+1, case(c, f, x)))
