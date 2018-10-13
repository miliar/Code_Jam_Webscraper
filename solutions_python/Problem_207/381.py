def calc(file):
    n, r, o, y, g, b, v = map(int, file.readline().split())
    ans = []
    if 2 * r > n or 2*y > n or 2*b > n:
        return "IMPOSSIBLE"
    d = sorted ([["R", r], ["Y", y], ["B", b]], key=lambda x: x[1], reverse=True)
    diff = d[1][1] - d[2][1]
    for _ in xrange(diff):
        ans.append(d[0][0])
        ans.append(d[1][0])
        d[0][1] -= 1
        d[1][1] -= 1

    diff = d[0][1]/2
    for _ in xrange(diff):
        ans.append(d[0][0])
        ans.append(d[1][0])
        ans.append(d[0][0])
        ans.append(d[2][0])
        d[0][1] -= 2
        d[1][1] -= 1
        d[2][1] -= 1

    if d[0][1] > 0:
        ans.append(d[0][0])
        d[0][1] -= 1

    diff = d[1][1]
    for _ in xrange(diff):
        ans.append(d[1][0])
        ans.append(d[2][0])
        d[1][1] -= 1
        d[2][1] -= 1

    return "".join(ans)

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t + 1) + ": " + str(ans) + "\n")
    fl_o.close()


main()