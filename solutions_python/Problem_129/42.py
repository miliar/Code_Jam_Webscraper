class Sta:
    num = 0
    type = 0
    la = None
    pos = 0

    def __init__(self, pos, type, num):
       self.num = num
       self.type = type
       self.pos = pos

def cc(n, i):
    return n*(n+1)/2 - (n-i)*(n+1-i)/2

def solve(S, n, m, ans):
    S.sort(key = lambda x : x.pos * 10 + x.type)
    la = None
    for t in S:
        #print (t.pos, t.type, t.num)
        if t.type == 0:
            t.la = la
            la = t
        else:
            while la and la.num <= t.num:
                t.num -= la.num
                ans -= cc(n, t.pos - la.pos) * la.num
                la.num = 0
                la = la.la
            if t.num > 0:
                la.num -= t.num
                ans -= cc(n, t.pos - la.pos) * t.num
                t.num = 0
    return ans

with open("input.txt","r") as in_file:
    i = 0
    cst = 0
    ttt = 0
    S = []
    n = 0
    m = 0
    ans = 0
    for row in in_file:
        if (i!=0):
            line = row.split()
            if (cst==0):
                n = int(line[0])
                m = int(line[1])
                ans = 0
                S = []
                cst = m
            else:
                cst-=1
                S.append(Sta(int(line[0]), 0, int(line[2])))
                S.append(Sta(int(line[1]), 1, int(line[2])))
                ans += cc(n, int(line[1]) - int(line[0])) * int(line[2])
                if (cst==0):
                    ttt+=1
                    print "Case #%d: %d"%(ttt, solve(S, n, m, ans))
        i+=1
