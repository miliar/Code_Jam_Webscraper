import heapq

def split(n):
    if n % 2 == 1:
        return ((n - 1) // 2, (n - 1) // 2)
    else:
        return (n // 2 - 1, n // 2)
    
def solve_one(n, k):
    heap = [-n]
    for i in range(k - 1):
        top = -heapq.heappop(heap)
        for a in split(top):
            if a != 0:
                heapq.heappush(heap, -a)
    top = -heapq.heappop(heap)
    return max(split(top)), min(split(top))


def solve(data, f):
    lines = data.split("\n")
    T = int(lines[0])
    ncase = 0
    for line in lines[1:(T + 1)]:
        ncase += 1
        n, k = tuple(int(x) for x in line.split())
        ans = solve_one(n, k)
        f.write("Case #%d: %d %d\n" % (ncase, ans[0], ans[1]))

def solve_files(infile, outfile):
    data = open(infile, "rt").read()
    with open(outfile, "wt") as f:
        solve(data, f)


    
