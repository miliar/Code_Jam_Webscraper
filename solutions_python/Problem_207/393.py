

def is_ok(cs):
    if cs[0] == cs[-1]:
        return False
    for i in range(len(cs)-1):
        if cs[i] == cs[i+1]:
            return False
    return True

def solve_small(n_col):
    """N stables, and colors. Place unicorns such that no neighbors have same base color in mane."""
    n = n_col[0]
    r, o, y, g, b, v = n_col[1:]
    if not(o == 0 and g == 0 and v == 0):
        return "NOT_SUPPORTED"
    ryb = sorted([(r, 'R'), (y, 'Y'), (b, 'B')], reverse=True)
    cs = ['?'] * n
    cs[0] = ryb[0][1]
    ryb[0] = ryb[0][0] - 1, ryb[0][1]
    ryb = sorted(ryb, reverse=True)
    for i in range(1, len(cs)):
        if ryb[0][1] == cs[i-1]:
            cs[i] = ryb[1][1]
            ryb[1] = (ryb[1][0] - 1, ryb[1][1])
            if ryb[1][0] < 0:
                return "IMPOSSIBLE"
        else:
            cs[i] = ryb[0][1]
            ryb[0] = (ryb[0][0] - 1, ryb[0][1])
        ryb = sorted(ryb, reverse=True)
    assert sum(c[0] for c in ryb) == 0
    assert len(cs) == n
    if is_ok(cs):
        return ''.join(cs)
    else:
        # try flip last two
        cs[-1], cs[-2] = cs[-2], cs[-1]
        if is_ok(cs):
            return ''.join(cs)
        else:
            return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
  n_col = list(map(int, input().split(" ")))
  print("Case #{}: {}".format(i, solve_small(n_col)))
