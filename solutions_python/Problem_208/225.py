import sys

def solve(n, horses, routes, u, v):
    fastest = int(1e100)
    status = (u, horses[u][0], horses[u][1])
    used = set([u])
    todo = [(0, status, used)]
    while len(todo) > 0:
        t, status, used = todo.pop()
        i, e, s = status
        for j, d in routes[i]:
            new_e = e - d
            if new_e < 0: # Horse cannot make it
                continue
            new_t = t + (d / s)
            if j == v: # Arrived
                fastest = min(fastest, new_t)
                continue
            # Reuse horse
            new_status = (j, new_e, s)
            todo.append((new_t, new_status, used))
            # Use new horse
            if j not in used: # Horse not already used
                new_used = set(used)
                new_used.add(j)
                new_status = (j, horses[j][0], horses[j][1])
                todo.append((new_t, new_status, new_used))
    return fastest

tc_len = int(sys.stdin.readline())

for tc in range(tc_len):
    n, q = tuple(int(x) for x in sys.stdin.readline().split())
    horses = []
    routes = [[] for _ in range(n)]
    for _ in range(n):
        e, s = tuple(int(x) for x in sys.stdin.readline().split())
        horses.append((e, s))
    for i in range(n):
        distances = tuple(int(x) for x in sys.stdin.readline().split())
        for j, distance in enumerate(distances):
            if distance == -1:
                continue
            routes[i].append((j, distance))
    results = []
    for _ in range(q):
        u, v = tuple(int(x) for x in sys.stdin.readline().split())
        results.append(solve(n, horses, routes, u - 1, v - 1))
    print('Case #' + str(tc + 1) + ': ' + ' '.join(str(x) for x in results))
