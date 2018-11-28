import heapq


def input(fname):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            lines.append(line[:-1])
    return lines


def solve(line):
    n, rem = map(int, line.split())
    h = [-n]
    d = {n: 1}
    seen = {n,}
    mx=mn=n
    while rem > 0:
        cur = -heapq.heappop(h)
        k = d[cur]
        cnt = min(k, rem)
        mx = cur//2
        d[mx] = d.get(mx, 0) + cnt
        mn = (cur-1)//2
        d[mn] = d.get(mn, 0) + cnt
        if mx not in seen:
            heapq.heappush(h,-mx)
            seen.add(mx)
        if mn not in seen:
            heapq.heappush(h,-mn)
            seen.add(mn)
        rem -= cnt
    return mx, mn


def main():
    lines = input('C-large.in')
    for c, line in enumerate(lines[1:]):
        mx, mn = solve(line)
        print "Case #{}: {} {}".format(c+1, mx, mn)

if __name__ == "__main__":
    main()