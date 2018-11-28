import sys
import itertools

def DFS(v, visited, graph):
    "Depth-first search through graph, appending current node when returning"
    if visited[v]:
        return []
    visited[v] = True
    output = []
    for w in graph[v]:
        output += DFS(w, visited, graph)
    output.append(v)
    return output

def BuildComponents(v, C, visited, reverseGraph):
    "Build components from reverseGraph"
    if visited[v]:
        return C
    visited[v] = True
    if -v in C:
        raise Exception()
    if v not in C:
        C[v] = True
    for w in reverseGraph[v]:
        BuildComponents(w, C, visited, reverseGraph)
    return C

def TwoSAT(Q, n):
    """Calculate 2SAT for query Q with n variables.
    Returns None if no solution, else an object with variable index as key and
    boolean as value."""
    graph = []
    reverseGraph = []
    for i in range((n+1)*2):
        graph.append([])
        reverseGraph.append([])
    for (a, b) in Q:
        graph[-a].append(b)
        graph[-b].append(a)
        reverseGraph[a].append(-b)
        reverseGraph[b].append(-a)
    visited = [False] * ((n+1)*2)
    order = []
    for i in range(n):
        order += DFS(i+1, visited, graph)
        order += DFS(-(i+1), visited, graph)
    order = order[::-1]
    visited = [False] * ((n+1)*2)
    components = []
    try:
        for v in order:
            components.append(BuildComponents(v, {}, visited, reverseGraph))
    except:
        return
    values = {}
    while len(values) < n:
        c = components.pop()
        for p in c:
            if abs(p) not in values:
                values[abs(p)] = abs(p) == p
    return values

sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ R, C ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  rows = []
  for r in xrange(R):
    rows.append(list(sys.stdin.readline().strip()))

  vs = set()
  vert, horiz = set(), set()
  pairs = []
  ok = True
  for r in xrange(R):
    for c in xrange(C):
      if rows[r][c] == '#': continue
      rrs, ccs = [], []
      for rr in xrange(r, R):
        if rows[rr][c] == '#': break
        if rows[rr][c] == '-' or rows[rr][c] == '|': rrs.append(rr)
      for rr in reversed(xrange(r)):
        if rows[rr][c] == '#': break
        if rows[rr][c] == '-' or rows[rr][c] == '|': rrs.append(rr)
      for cc in xrange(c, C):
        if rows[r][cc] == '#': break
        if rows[r][cc] == '-' or rows[r][cc] == '|': ccs.append(cc)
      for cc in reversed(xrange(c)):
        if rows[r][cc] == '#': break
        if rows[r][cc] == '-' or rows[r][cc] == '|': ccs.append(cc)

      for rr in rrs: vs.add((rr, c))
      for cc in ccs: vs.add((r, cc))
      if len(rrs) > 1:
        for rr in rrs: horiz.add((rr, c))
      if len(ccs) > 1:
        for cc in ccs: vert.add((r, cc))
      if rows[r][c] == '.':
        if len(rrs) == 1 and len(ccs) == 0:
          for rr in rrs: vert.add((rr, c))
        elif len(rrs) == 0 and len(ccs) == 1:
          for cc in ccs: horiz.add((r, cc))
        elif len(rrs) == 1 and len(ccs) == 1:
          pairs.append(((rrs[0], c), (r, ccs[0])))
        else:
          ok = False

  res = 0
  if ok:
    vss = {}
    rev = {}
    for v in vs:
      vss[v] = len(vss) + 1
      rev[vss[v]] = v
#    print vss
#    print vert, horiz
#    print pairs
    ors = []
    for v in vert:
      ors.append((vss[v], vss[v]))
    for v in horiz:
      ors.append((-vss[v], -vss[v]))
    for p, q in pairs:
      ors.append((vss[p], -vss[q]))

#    print ors
    twoS = TwoSAT(ors, len(vss))
#    print rev
#    print twoS
    if twoS is None: ok = False
    else:
      for idx, is_vert in twoS.iteritems():
        r, c = rev[idx]
        rows[r][c] = '|' if is_vert else '-'
  res = "POSSIBLE" if ok else "IMPOSSIBLE"
  print "Case #%d: %s" % (1+tmp_tc, res)
  if ok:
    for r in rows:
      print ''.join(r)
#print TwoSAT([ (-1, -1), (1, 2) ], 2)
