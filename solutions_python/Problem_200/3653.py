def is_tidy(N):
    print(N)
    valid = True
    last = '0'
    for c in N:
        print(c)
        if c < last:
            valid = False
            break
        last = c
    return valid
f = open('./B-small-attempt0.in', 'r')
w = open('./B-small-attempt0.out', 'w')
T = int(f.readline())
for i in range(T):
    N = int(f.readline())
    res = N
    while not is_tidy(str(res)):
        res-=1
    w.write("Case #%i: %i\n" % (i+1,res))
