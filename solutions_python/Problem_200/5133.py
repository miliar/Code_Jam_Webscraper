t = int(raw_input())
for r in range(t):
    N = int(raw_input())
    def is_tidy(x):
        q = str(x)
        for y in range(len(q)-1):
            if int(q[y]) > int(q[y+1]):
                return False
        return True
    found = False
    n = N
    for x in range(N,0,-1):
        if (not(found)):
            if is_tidy(x):
                found = True
                n = x
    print("Case #{}: {}".format(r+1,n))