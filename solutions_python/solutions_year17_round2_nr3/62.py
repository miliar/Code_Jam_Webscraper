

def solve_small(horses, cities, mail):
    # assuming small input
    dists = [0]*len(cities)
    sumdists = [0]*len(cities)
    for city in range(len(cities) - 1):
        dists[city + 1] = cities[city][city+1]
        sumdists[city + 1] = dists[city + 1] + sumdists[city]
    table = [0]
    for dst in range(1, len(cities)):
        best = None
        for src in range(0, dst):
            maxdist, speed = horses[src]
            if maxdist >= sumdists[dst] - sumdists[src]:
                time = table[src] + (sumdists[dst] - sumdists[src]) / speed
                best = time if best is None else min(best, time)
        if best is None:
            return "IMPOSSIBLE"
        table.append(best)
    return table[len(cities) - 1]

def create_table(n,m,default=0):
    return [m*[default] for i in range(n)]

def all_pairs_shortest_path(cities):
    table = create_table(len(cities), len(cities), float("Inf"))
    for city in range(len(cities)):
        table[city][city] = 0
    for src in range(len(cities)):
        for dst in range(len(cities)):
            if cities[src][dst] != -1:
                table[src][dst] = cities[src][dst]
    for through in range(len(cities)):
        for src in range(len(cities)):
            for dst in range(len(cities)):
                if table[src][through] + table[through][dst] < table[src][dst]:
                    table[src][dst] = table[src][through] + table[through][dst]
    return table

def solve(horses, cities, mail):
    dist = all_pairs_shortest_path(cities)
    table = create_table(len(cities), len(cities), float("Inf"))
    for city in range(len(cities)):
        table[city][city] = 0
    for src in range(len(cities)):
        for dst in range(len(cities)):
            maxdist, speed = horses[src]
            if dist[src][dst] <= maxdist:
                table[src][dst] = dist[src][dst] / speed
    for through in range(len(cities)):
        for src in range(len(cities)):
            for dst in range(len(cities)):
                maxdist, speed = horses[src]
                if table[src][through] + table[through][dst] < table[src][dst]:
                    table[src][dst] = table[src][through] + table[through][dst]
    result = []
    for src, dst in mail:
        result.append(table[src - 1][dst - 1])
    return ' '.join(map(str, result))

def main():
    cases = int(input())
    for case in range(1, cases+1):
        city_count, mail_count = tuple(int(x) for x in input().rstrip().split(" "))
        horses = []
        for _ in range(city_count):
            horses.append(tuple(int(x) for x in input().rstrip().split(" ")))
        cities = []
        for _ in range(city_count):
            cities.append(list(int(x) for x in input().rstrip().split(" ")))
        mail = []
        for _ in range(mail_count):
            mail.append(tuple(int(x) for x in input().rstrip().split(" ")))
        print("Case #%d: %s" % (case, solve(horses, cities, mail)))

if __name__ == '__main__':
    main()

        