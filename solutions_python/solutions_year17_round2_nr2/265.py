#Henry Maltby
#Code Jam 2017

def stable_neighbors(r, y, b):
    """
    .
    """
    if 2 * max(r, y, b) > r + y + b:
        return "IMPOSSIBLE"
    if max(r, y, b) == r:
        ans = "RBY" * (b + y - r) + "RY" * (r - b) + "RB" * (r - y)
    if max(r, y, b) == y:
        ans = "YBR" * (b + r - y) + "YB" * (y - r) + "YR" * (y - b)
    if max(r, y, b) == b:
        ans = "BRY" * (r + y - b) + "BR" * (b - y) + "BY" * (b - r)
    return ans

def B():
    """
    Runs the problem as dictated in problem spec.
    """
    f = open('B-small-attempt0.in')
    g = open('B-small-attempt0.out', 'w')

    T = int(f.readline())
    for i in range(T):
        N, R, O, Y, G, B, V = [int(x) for x in f.readline().strip().split(' ')]
        ans = stable_neighbors(R, Y, B)
        g.write("Case #" + str(i + 1) + ": " + ans)
        if i != T - 1:
            g.write("\n")

B()
