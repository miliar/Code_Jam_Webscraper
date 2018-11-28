
# - is 0, | is 1

def notd(c):
    return '|' if c == '-' else '-'

def solve(clauses, variables):
    out_edges = {}
    in_edges = {}
    visited = set()
    for var in variables:
        out_edges[(var, '-')] = []
        out_edges[(var, '|')] = []
        in_edges[(var, '-')] = []
        in_edges[(var, '|')] = []
    for cl in clauses.values():
        if cl['-'] is None or cl['|'] is None:
            assert cl['|'] or cl['-'] is not None
            var, d = cl['|'] or cl['-']
            out_edges[(var, notd(d))].append((var, d))
            in_edges[(var, d)].append((var, notd(d)))
        else:
            var1, d1 = cl['-']
            var2, d2 = cl['|']
            out_edges[(var1, notd(d1))].append((var2, d2))
            in_edges[(var2, d2)].append((var1, notd(d1)))
            out_edges[(var2, notd(d2))].append((var1, d1))
            in_edges[(var1, d1)].append((var2, notd(d2)))
    L = []
    def visit(u):
        if u not in visited:
            visited.add(u)
            for neib in out_edges[u]:
                visit(neib)
            L.append(u)
    for var in variables:
        for d in '-|':
            visit((var, d))
    L.reverse()
    comps = [] # topological ordering of components
    component_label = {}
    comp_to_vars = {}
    def assign(u, root):
        if u not in component_label:
            component_label[u] = root
            comp_to_vars[root].append(u)
            for neib in in_edges[u]:
                assign(neib, root)
    for u in L:
        if u not in component_label:
            comps.append(u)
            comp_to_vars[u] = []
        assign(u, u)

    #print(component_label)
    for var in variables:
        if component_label[(var, '-')] == component_label[(var, '|')]:
            return None

    assignment = {}
    for comp in reversed(comps):
        cvar, cd = comp
        if cvar not in assignment:
            for var, d in comp_to_vars[comp]:
                assert var not in assignment
                assignment[var] = d
    for var in variables:
        if var not in assignment:
            assignment[var] = '|'
    return assignment

def add(p1, p2):
    return (p1[0] + p2[0], p1[1]+p2[1])

def inbounds(grid, loc):
    return 0 <= loc[0] < len(grid[0]) and 0 <= loc[1] < len(grid)

def mirror(delta, m):
    if m == '/':
        return (-delta[1], -delta[0])
    elif m == '\\':
        return (delta[1], delta[0])

def trace(grid, loc, delta):
    hits = []
    while True:
        loc = add(loc, delta)
        if not inbounds(grid, loc):
            break
        c = grid[loc[1]][loc[0]]
        if c == '-' or c == '|':
            return hits, True
        elif c == '.':
            hits.append((loc, '-' if delta[1] == 0 else '|'))
        elif c == '#':
            break
        elif c == '/' or c == '\\':
            delta = mirror(delta, c)
    return hits, False

def run_test():
    R, C = map(int, input().split())
    initial_grid = [input() for y in range(R)]
    for row in initial_grid:
        assert len(row) == C

    clauses = {}
    for y, row in enumerate(initial_grid):
        for x, c in enumerate(row):
            if c == '.':
                clauses[(x, y)] = {'-':None, '|':None}
    variables = []
    for y, row in enumerate(initial_grid):
        for x, c in enumerate(row):
            if c == '-' or c == '|':
                variables.append((x, y))
    for var in variables:
        dashr_hits, dashr_failure = trace(initial_grid, var, (1, 0))
        dashl_hits, dashl_failure = trace(initial_grid, var, (-1, 0))
        pipeu_hits, pipeu_failure = trace(initial_grid, var, (0, -1))
        piped_hits, piped_failure = trace(initial_grid, var, (0, 1))
        dash_failure = dashr_failure or dashl_failure
        pipe_failure = pipeu_failure or piped_failure
        if dash_failure and pipe_failure:
            return 'IMPOSSIBLE'
        if dash_failure:
            clauses[var] = {'-':(var, '|'), '|':None}
        if pipe_failure:
            clauses[var] = {'-':(var, '-'), '|':None}
        for l, b, d in [(dashr_hits + dashl_hits,
                         dash_failure, '-'),
                        (pipeu_hits + piped_hits,
                         pipe_failure, '|')]:
            if not b:
                for loc, locd in l:
                    assert clauses[loc][locd] is None
                    clauses[loc][locd] = (var, d)
    for cl in clauses.values():
        if cl['-'] is None and cl['|'] is None:
            return 'IMPOSSIBLE'
    assignment = solve(clauses, variables)
    if assignment is None:
        return 'IMPOSSIBLE'
    else:
        out = ['POSSIBLE']
        for y, row in enumerate(initial_grid):
            rows = ''.join(assignment[(x, y)] if c == '-' or c == '|' else c
                           for x, c in enumerate(row))
            out.append(rows)
        return '\n'.join(out)

for i in range(1, int(input()) + 1):
    ans = run_test()
    print("Case #{}: {}".format(i, ans))
