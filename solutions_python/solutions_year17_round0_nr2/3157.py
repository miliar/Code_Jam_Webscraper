def helper(arr):
    sol = arr[:]
    d = len(sol)
    x = True
    for i in range(0,d-1):
        if x:
            if sol[i] <= sol[i+1]:
                pass
            else:
                sol[i] = sol[i] - 1
                x = False
        else:
            sol[i] = 9
    if (sol[-1] < sol[-2]) or not x:
        sol[-1] = 9
    return sol   


def helper2(arr):
    d = len(arr)
    return sum([arr[i] * 10**(d-i-1) for i in range(d)])
        

def sol(s):
    d = len(s)
    if d == 1:
        return int(s)

    arr = [int(c) for c in s]
    while arr != helper(arr):
        arr = helper(arr)        
    return helper2(arr)

t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    print "Case #%d: %d" % (a0+1,sol(n))
