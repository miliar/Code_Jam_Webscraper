T = int(input())

def solve():
    N,R,_,Y,_,B,_ = [int(x) for x in input().split()]
    s = [(R,'R'), (Y,'Y'), (B,'B')]
    s.sort(reverse = True)
    s = [[a,b] for (a,b) in s]
    res = s[1][0] + s[2][0] - s[0][0]
    if res < 0:
        return "IMPOSSIBLE"
    ss = []
    for _ in range(s[0][0]):
        ss.append(s[0][1])
        if s[1][0] > 0:
            ss.append(s[1][1])
            s[1][0] -= 1
            if res > 0:
                ss.append(s[2][1])
                res -= 1
        else:
            ss.append(s[2][1])
    return "".join(ss)

for t in range(T):
    print("Case #%d: %s" % (t+1, solve()))
