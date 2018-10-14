def solve(s):
    n = len(s)
    if n==1 and s[0]==0:
        return []
    elif n==1:
        return s
    for i in xrange(n-1):
        if s[i]<=s[i+1]:
            pass
        else:
            s[i] -= 1
            return solve(s[:i+1])+[9]*(n-i-1)
    return s

if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case < t:
        case += 1
        s = raw_input()
        print "Case #" + str(case) + ":","".join(map(str,solve(map(int,s))))

