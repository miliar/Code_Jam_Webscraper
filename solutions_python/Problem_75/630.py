fIn = open("B.in", "r")
fOut = open("B.out", "w")

T = int(fIn.readline())
for i in range(1, T+1):
    li = fIn.readline().split(" ")
    pos = 0
    C = int(li[pos])
    pos += 1
    comb = []
    dest = []
    for c in range(C):
        comb.append(li[pos])
        pos += 1
    D = int(li[pos])
    pos += 1
    for d in range(D):
        dest.append(li[pos])
        pos += 1
    N = int(li[pos])
    pos += 1
    ele = li[pos]
    ele = ele[:len(ele)-1]
    pos += 1
    cur = []
    def combine(e1, e2):
        for c in comb:
            if c[0] == e1 and c[1] == e2:
                return c[2]
            elif c[0] == e2 and c[1] == e1:
                return c[2]
        return None
    def destroy(e1, e2):
        for c in dest:
            if c[0] == e1 and c[1] == e2:
                return True
            elif c[0] == e2 and c[1] == e1:
                return True
        return False
    for c in ele:
        if cur == []:
            cur.append(c)
        else:
            bl = combine(cur[len(cur)-1], c)
            if not bl is None:
                cur.pop()
                cur.append(bl)
            else:
                done = False
                for t in cur:
                    if destroy(t, c):
                        cur = []
                        done = True
                        break
                if not done:
                    cur.append(c)
    ans = "Case #%d: " % (i,)
    ans += "[" + ", ".join(cur) + "]\n"
    fOut.write(ans)

fOut.close();
