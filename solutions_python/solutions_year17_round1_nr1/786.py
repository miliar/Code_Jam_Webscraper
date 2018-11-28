def bfs(starts, pendings, m, r, c):
    # print starts, pendings
    for n in starts:
        added = 0
        low = -1
        high = -1
        i = starts[n][0]
        j = starts[n][1]
        for jj in range(j + 1, c):
            if m[i][jj] == "?":
                m[i][jj] = n
                high = jj
                added += 1
                pendings.remove((i, jj))
            else:
                break
        for jj in range(j - 1, -1, -1):
            if m[i][jj] == "?":
                m[i][jj] = n
                low = jj
                added += 1
                pendings.remove((i, jj))
            else:
                break
        if added:
            starts[n][2] = "R"
            if high == -1:
                high = j
            if low == -1:
                low = j
            starts[n][3] = low
            starts[n][4] = high
            continue
        for ii in range(i + 1, r):
            if m[ii][j] == "?":
                m[ii][j] = n
                high = ii
                added += 1
                pendings.remove((ii, j))
            else:
                break
        for ii in range(i - 1, -1, -1):
            if m[ii][j] == "?":
                m[ii][j] = n
                low = ii
                added += 1
                pendings.remove((ii, j))
            else:
                break
        if added:
            starts[n][2] = "C"
            if high == -1:
                high = i
            if low == -1:
                low = i
            starts[n][3] = low
            starts[n][4] = high



def solve(starts, pendings, m, r, c):
    for n in starts:
        i = starts[n][0]
        j = starts[n][1]
        low = starts[n][3]
        high = starts[n][4]
        if starts[n][2] == "C":
            added = 0
            for j2 in range(j + 1, c):
                suc = 1
                for i2 in range(low, high+1):
                    if m[i2][j2] != "?":
                        suc = 0
                        break
                if not suc:
                    break
                print i, j, n
                for i2 in range(low, high+1):
                    m[i2][j2] = n
            for j2 in range(j - 1, -1, -1):
                suc = 1
                for i2 in range(low, high+1):
                    if m[i2][j2] != "?":
                        suc = 0
                        break
                if not suc:
                    break
                print i, j, n
                for i2 in range(low, high+1):
                    m[i2][j2] = n
        if starts[n][2] == "R":
            added = 0
            for i2 in range(i + 1, r):
                suc = 1
                for j2 in range(low, high+1):
                    if m[i2][j2] != "?":
                        suc = 0
                        break
                if not suc:
                    break
                print i, j, n
                for j2 in range(low, high+1):
                    m[i2][j2] = n
            for i2 in range(i - 1, -1, -1):
                suc = 1
                for j2 in range(low, high+1):
                    if m[i2][j2] != "?":
                        suc = 0
                        break
                if not suc:
                    break
                # print i, j, n
                for j2 in range(low, high+1):
                    m[i2][j2] = n


def calc(m, r, c):
    # print m
    pendings = set()
    starts = {}
    for i in range(r):
        for j in range(c):
            if m[i][j] == "?":
                pendings.add((i,j))
            else:
                starts[m[i][j]] = [i,j, "N", 0, 0]
    bfs(starts, pendings, m, r, c)
    solve(starts, pendings, m, r, c)
    # print starts

    ret = ""
    for l in m:
        ret += "".join(l)
        ret += "\n"
    return ret[:-1]

def main():
    inpfile = open("A-small-attempt0.in", 'r')
    outfile = open('output', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        line = inpfile.readline().strip()
        linelst = line.split()
        r = int(linelst[0])
        c = int(linelst[1])
        m = []
        for i in range(r):
            line = inpfile.readline().strip()
            linelst = list(line)
            m.append(linelst)
        ret = calc(m, r, c)
        
        result = "Case #%s:\n%s\n" % (case, ret)
        print result
        outfile.write(result)
    inpfile.close()
    outfile.close()



if __name__ == "__main__":
    
    main()
    
