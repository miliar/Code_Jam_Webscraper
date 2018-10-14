
def is_tidy(n):
    ds = [int(d) for d in list(str(n))]
    i = 0
    tidy = True
    while tidy and i+1 < len(ds):
        tidy = ds[i] <= ds[i+1]
        i += 1
    #print('  n:{}'.format(n))
    if n % 10 == 0:
        extra = 1
    else:
        extra = int(str(n)[i:])+1
    #if not tidy:
    #    print('ext:{}'.format(extra))
    return (tidy, extra)
    
def doit(N):
    curr = N
    (tidy, extra) = is_tidy(curr)
    while not tidy:
        curr -= extra
        (tidy, extra) = is_tidy(curr)
    return curr

t = int(input())
for i in range(1, t+1):
    N = int(input())
    out = doit(N)
    print('Case #{}: {}'.format(i, out))

