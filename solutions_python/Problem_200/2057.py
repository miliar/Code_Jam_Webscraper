def solve( n ):
    s = str(n)
    if len(s) == 1:
        return s
    t = 0
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            t = i
            s = s[:i] + str(int(s[i]) - 1) + '9' * (len(s) - i-1)
            break
    if t == 0:
        if s[t] > s[t+1]:
            return str(int(s[0])-1) + '9'*(len(s)-1)
        else:
            return s
    else:
        p = t
        for i in range(t, 0, -1):
            if s[i-1] > s[i]:
                p = i-1
                s = s[:p] + str( int(s[p]) - 1) + '9'*(len(s) - p-1)
        return s

t = int(input())

for i in range(1, t+1):
    n = input()
    s = solve(n)
    s = str(int(s))
    print( "Case #{}: {}".format(i, s) )
