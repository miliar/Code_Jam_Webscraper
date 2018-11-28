__author__ = 'Roberto'

class FreeFormBfsGraph:
    def __init__(self, nodes, get_neighbours):

        self.nodes = nodes
        self.get_neighbours = get_neighbours

    def breadth_first_search(self, starting_node, horse):

        from collections import deque

        queue = deque([])
        queue.append((starting_node, horse[0]))
        visited = {}

        edges = []

        while len(queue) > 0:

            current_node, remaining_stamina = queue.popleft()

            if remaining_stamina < 0:
                continue

            if current_node in visited:
                continue
            visited[current_node] = True


            if current_node != starting_node:
                distance = horse[0] - remaining_stamina
                time = distance / horse[1]
                edges.append((current_node, time))

            for next_node, distance in self.get_neighbours(current_node):
                queue.append((next_node, remaining_stamina - distance))


        return edges

def Dijsktra(adj, source, target):

    import heapq

    heap = []
    visited = {}

    heapq.heappush(heap, (0, source))

    while len(heap) > 0:

        cost, where = heapq.heappop(heap)

        if where in visited:
            continue
        visited[where] = True

        if where == target:

            return cost

        for next, c in adj[where]:
            heapq.heappush(heap, (cost + c, next))

    return -1

def finish(index, solution):

    print(solution)

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def solve_test(index, horses, routes, queries):

    debug_out.write("Case #{0} In: {1} {2} {3} Out: ".format(index, horses, routes, queries))

    print("Case: [{0} {1} {2}]".format(horses, routes, queries))

    n = len(horses)
    routes = [[(i, distance) for i, distance in enumerate(map(int, line.split())) if distance > -1] for line in routes]
    horses = [tuple(map(int, line.split())) for line in horses]

    dijsktra_edges = []
    graph = FreeFormBfsGraph(list(range(n)), lambda n: routes[n])
    for i in range(n):
        edges = graph.breadth_first_search(i, horses[i])
        dijsktra_edges.append(edges)

    is_dijsktra = True
    if is_dijsktra:

        results = []
        for query in queries:

            f, t = map(int, query.split())
            cost = Dijsktra(dijsktra_edges, f-1, t-1)
            results.append(cost)

        finish(index, " ".join(map(str, results)))
    else:
        infinity = 10000000000000
        adj = [[infinity] * n for _ in range(n)]
        for i in range(n):
            for j, distance in dijsktra_edges[i]:
                adj[i][j] = distance

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

        results = []
        for query in queries:

            f, t = map(int, query.split())
            results.append(adj[f-1][t-1])

        finish(index, " ".join(map(str, results)))


if __name__ == "__main__":
    task = "C"
    level = 1
    attempts = 1

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]
    j = 0
    for i in range(0, number_of_lines):

        N, Q = map(int, test_cases[j].split())
        j += 1
        horses = test_cases[j : j + N]
        j += N
        routes = test_cases[j : j + N]
        j += N
        queries = test_cases[j : j + Q]
        j += Q
        solve_test(i, horses, routes, queries)

    file_out.close()