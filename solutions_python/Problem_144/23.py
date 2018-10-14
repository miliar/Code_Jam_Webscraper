import fileinput

__author__ = 'psmit'


def search(visited, stack, connections, cities):
    if len(visited) == len(cities):
        return tuple(visited)

    results = []
    for c in cities:
        if c not in visited and (stack[-1],c) in connections:
            result = search(visited + [c], stack + [c], connections, cities)
            if result is not None:
                results.append(result)

    if len(stack) > 1:
        result = search(visited, stack[:-1], connections, cities)
        if result is not None:
            results.append(result)

    if len(results) > 0:
        return min(results)
    else:
        return None




def main():

    inp = fileinput.input()

    T = int(inp.readline())

    for t in range(1,T+1):
        cities = [0]
        connections = set()

        N,M = (int(x) for x in inp.readline().split())
        for _ in range(N):
            cities.append(inp.readline().strip())
        for _ in range(M):
            i,j = (int(x) for x in inp.readline().split())

            connections.add((cities[i], cities[j]))
            connections.add((cities[j], cities[i]))

        cities = sorted(cities[1:])
        result = None
        for c in cities:
            result = search([c], [c], connections, cities)
            if result is not None:
                break
        print("Case #{}: {}".format(t, "".join(result)))



main()