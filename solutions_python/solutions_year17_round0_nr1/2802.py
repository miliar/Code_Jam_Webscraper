import sys

sys.setrecursionlimit(20000000)


def convert(s):
    newS = ''
    for i in s:
        if i=='-':
            newS += '+'
        else:
            newS += '-'
    return newS


def solve(s,c):
    n = len(s)
    if n<c:
        return float('inf')
    s = s.lstrip('+')
    if len(s)==0:
        return 0
    else:
        return 1 + solve(convert(s[:c]) + s[c:],c)



if __name__=="__main__":
    t = int(raw_input().strip())
    case = 0
    while case < t:
        case += 1
        s,c = raw_input().strip().split(" ")
        ans = solve(s, int(c))
        if ans ==float('inf'):
            print "Case #" + str(case) + ":","IMPOSSIBLE"
        else:
            print "Case #" + str(case) + ":", ans

