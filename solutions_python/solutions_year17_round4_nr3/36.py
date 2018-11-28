import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))

def traceimpl(G, r, c, dr, dc):
    ret = set()
    while True:
        r += dr
        c += dc
        if r < 0 or r >= len(G): return ret
        if c < 0 or c >= len(G[0]): return ret
        if G[r][c] == "#": return ret
        if G[r][c] == "/":
            dr, dc = -dc, -dr
            continue
        if G[r][c] == "\\":
            dr, dc = dc, dr
            continue
        if G[r][c] == '-' or G[r][c] == '|': return None
        ret.add((r,c))

def tracepath(G, r, c):
    # Vert:
    up = traceimpl(G, r, c, -1, 0)
    down = traceimpl(G, r, c, 1, 0)
    vert = None
    if up is not None and down is not None:
        vert = up | down

    # Hor:
    right = traceimpl(G, r, c, 0, 1)
    left = traceimpl(G, r, c, 0, -1)
    hor = None
    if right is not None and left is not None:
        hor = left | right

    return vert, hor

def resolve(beams, e):
    empty = set(e)
    left = {}
    resolved = {}

    only = {}
    for loc, cover in beams.iteritems():
        if cover[0] is None and cover[1] is None:
            return None
        if cover[0] is None:
            resolved[loc] = "-"
            empty -= cover[1]
            continue
        if cover[1] is None:
            resolved[loc] = "|"
            empty -= cover[0]
            continue
        for place in cover[0]:
            if place in only:
                only[place] = None
            else:
                only[place] = loc, '|'
        for place in cover[1]:
            if place in only:
                only[place] = None
            else:
                only[place] = loc, '-'
        left[loc] = cover

    savedEmpty = set(empty)
    for e in savedEmpty:
        if e not in only:
            return None
        i = only[e]
        if i is None: continue
        loc, res = i
        if loc in resolved:
            if resolved[loc] != res:
                return None
            continue
        resolved[loc] = res
        empty -= left[loc][0] if res == '|' else left[loc][1]
        del left[loc]

    if left:
        # Guess
        for loc, cover in left.iteritems():
            # Try vert
            newleft = {l:c for l,c in left.iteritems() if l != loc}
            newempty = empty - cover[0]
            test = resolve(newleft, newempty)
            if test is not None:
                resolved.update(test)
                resolved[loc] = '|'
                return resolved
            newempty = empty - cover[1]
            test = resolve(newleft, newempty)
            if test is not None:
                resolved.update(test)
                resolved[loc] = '-'
                return resolved
            return None
    return resolved

for case in range(1, cases + 1):
    line = inp.pop(0).strip()
    R, C = map(int, line.split())

    G = []
    for _ in range(R):
        G.append(list(i for i in inp.pop(0).strip()))

    empty = set()
    beams = {}
    for r in range(R):
        for c in range(C):
            if G[r][c] == '-' or G[r][c] == '|':
                beams[(r, c)] = tracepath(G, r, c)

            if G[r][c] == '.':
                empty.add((r,c))

    resolved = resolve(beams, empty)
    if resolved is None:
        result = "IMPOSSIBLE"
    else:
        result = "POSSIBLE\n"
        for (r,c), d in resolved.iteritems():
            G[r][c] = d
        result += "\n".join("".join(L) for L in G)
    print 'Case #{}: {}'.format(case, result)
