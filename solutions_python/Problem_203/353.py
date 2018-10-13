def calc(file, fl_o):
    r, c = map(int, file.readline().split())
    rc = []
    for _ in xrange(r):
        rc.append(list(file.readline().strip()))

    for i in xrange(r):
        for j in xrange(c):
            if rc[i][j] == "?":
                continue
            x = rc[i][j]
            k = j-1
            while k>=0 and rc[i][k] == "?":
                rc[i][k] = x
                k -= 1
            k = j+1
            while k < c and rc[i][k] == "?":
                rc[i][k] = x
                k += 1

    for j in xrange(c):
        for i in xrange(r):
            if rc[i][j] == "?":
                continue
            x = rc[i][j]
            k = i-1
            while k>=0 and rc[k][j] == "?":
                rc[k][j] = x
                k -= 1
            k = i+1
            while k < r and rc[k][j] == "?":
                rc[k][j] = x
                k += 1

    for i in xrange(r):
        fl_o.write( "".join(rc[i]) + "\n")


def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        fl_o.write("Case #" + str(t+1) + ":\n")
        ans = calc(file, fl_o)
    fl_o.close()

main()