import sys

DEBUG=True
DEBUG=False

def solve(n, colors):
    if DEBUG: print colors
    res = ""
    last_color = None
    for _ in xrange(n):
        colors.sort(key=lambda a: a[1])
        colors.sort(key=lambda a: a[0], reverse=True)
        idx = 0
        cnt, col = colors[0]
        if col == last_color:
            idx = 1
            cnt, col = colors[1]
        if DEBUG: print last_color, idx, colors
        if not cnt:
            return "IMPOSSIBLE"
        res += col
        if DEBUG: print res
        last_color = col
        colors[idx] = (cnt-1, col)
    if res[0] == res[-1]:
        res = res[0:-2] + res[-1] + res[-2]
    if res[-2] == res[-3]:
        return "IMPOSSIBLE"
    return res

if __name__ == "__main__":
    i = 1
    data = sys.stdin.read().split()
    for _ in xrange(int(data.pop(0))):
        n = int(data.pop(0))
        colors = [(int(data.pop(0)), "R"), (int(data.pop(0)), "O"), (int(data.pop(0)), "Y"), (int(data.pop(0)), "G"), (int(data.pop(0)), "B"), (int(data.pop(0)), "V")]
        print "Case #%d: %s" % (i, solve(n, colors))
        i += 1
