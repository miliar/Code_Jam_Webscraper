p = 0

def solv(a):
    global p

    if len(a) == 1:
        js = 0
        for i in range(len(a[0])):
            if len(a[0][i]) > 0:
                js+=1
        return js

    mm, MM = None, None
    for i in range(len(a)):
        m, M = 2000000, 1
        try:
            m = min(a[i][0])
            M = max(a[i][0])
        except ValueError:
            pass
        for j in range(1, len(a[0])):
            try:
                m = min(m, min(a[i][j]))
                M = max(M, max(a[i][j]))
            except ValueError:
                pass
        if m == 2000000:
            return 0

        if mm == None:
            mm = m
        else:
            mm = max(m, mm)
        if MM == None:
            MM = M
        else:
            MM = min(MM, M)
        if mm > MM:
            return 0
    p = 0
    def dfs(pairs):
        global p
        if p == len(a[0]):
            return
        if len(pairs) == len(a[0]):
            # print pairs
            p = max(p, reduce(lambda x,y: x+1 if y>=0 else x, pairs, 0))
            return
        i = len(pairs)
        noMatch = True
        si = set(a[0][i])
        for j in range(len(a[0])):
            if j not in pairs:
                s = si.intersection(set(a[1][j]))
                if len(s) > 0:
                    noMatch = False
                    dfs(pairs + [j])
        if noMatch:
            dfs(pairs+[-1])

    dfs([])
    return p

    


def get_ps(v, x):
    rtn = []
    i = v / x
    j = i+1
    while v <= j*x*11./10. and v >= j*x*9./10.:
        rtn.append(j)
        j += 1
    j = i
    while v <= j*x*11./10. and v >= j*x*9./10.:
        rtn.append(j)
        j -= 1
    return rtn

def proc(a, res):
    rtn = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            v = a[i][j]
            row.append(get_ps(v, res[i]))
        rtn.append(row)
    return rtn

def main():
    n = int(raw_input())
    for i in range(n):
        N, P = map(int, raw_input().split(' '))
        res = map(int, raw_input().split(' '))
        raw = []
        for j in range(N):
            row = map(int, raw_input().split(' '))
            raw.append(row)
        ans = solv(proc(raw, res))
        print "Case #%d: %d" %(i+1, ans)

if __name__ == "__main__":
    main()