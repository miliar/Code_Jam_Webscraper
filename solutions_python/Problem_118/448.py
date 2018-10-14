def is_palin(d):
    d = str(d)
    return all(d[i] == d[len(d)-i-1] for i in range(len(d)//2))

vals = list()

for i in range(3*10**6):
    if is_palin(i) and is_palin(i*i):
        vals.append(i*i)

tcs = int(input())

for tc in range(1, tcs+1):
    a, b = (int(i) for i in input().split(' '))
    print("Case #%d: %d" % (tc, len([i for i in vals if a <= i <= b])))
