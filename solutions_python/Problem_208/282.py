import queue


def answer(horses, direct_dists, queries):
    n = len(horses)

    infinity = 10000000000
    dists = [[infinity if direct_dists[u][v] == -1 else direct_dists[u][v] for v in range(n)] for u in range(n)]
    for u in range(n):
        for v in range(n):
            for k in range(n):
                dists[u][v] = min(dists[u][v], dists[u][k] + dists[k][v])

    results = []
    for u, v in queries:
        q = queue.PriorityQueue()
        q.put_nowait((0, u - 1))
        times = {}

        while not q.empty():
            time, city = q.get_nowait()
            if city in times:
                continue

            times[city] = time
            if city == v - 1:
                break
            for neighbor in range(0, n):
                if neighbor not in times and dists[city][neighbor] <= horses[city][0]:
                    q.put_nowait((time + dists[city][neighbor] / horses[city][1], neighbor))

        results.append(times[v - 1])

    return results


def main():
    t = int(input())
    for i in range(1, t + 1):
        n_str, q_str = input().split(" ")
        n = int(n_str)

        horses = []
        for j in range(n):
            e_str, s_str = input().split(" ")
            horses.append((int(e_str), int(s_str)))

        direct_dists = []
        for j in range(n):
            direct_dist = []
            ds_str = input().split(" ")
            for k in range(n):
                direct_dist.append(int(ds_str[k]))
            direct_dists.append(direct_dist)

        queries = []
        for j in range(int(q_str)):
            u_str, v_str = input().split(" ")
            queries.append((int(u_str), int(v_str)))

        result = answer(horses, direct_dists, queries)
        print("Case #{}: {}".format(i, " ".join(map(lambda r: "{:.8f}".format(r), result))))


if __name__ == "__main__":
    main()
