def solve(n,depth = 0):

    # find broken digit
    s = str(n)
    i = 0
    last = -1
    while i < len(s) and int(s[i]) >= last:
        last = int(s[i])
        i += 1

    if i == len(s):
        return n

    s = list(s)
    s[i-1] = str(int(s[i-1])-1)
    while i < len(s):
        s[i] = '9'
        i += 1
    partial_solution = int("".join(s))
    return(solve(partial_solution,depth+1))

T = int(input())
for t in range(T):
    n = int(input())
    print("Case #{0}: {1}".format(t+1,solve(n)))