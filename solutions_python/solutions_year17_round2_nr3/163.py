name = "C-small-attempt0"
input = name + ".in"
output = name + ".out"

def solve(n, q, e, s, d, u, v):
    """
    :param n: number of cities with horse
    :param q: number of requests
    :param e: energy of horse (total distance)
    :param s: speed of horse
    :param d: d[i][j] is distance from city i to city j
    :param u: start of requests
    :param v: stop of requests
    :return: 
    """
    # Small input set: straight line

    horses = [(0, e[0], s[0])]  # (time, energy, speed)
    for pos in range(1, n):
        dist = d[pos-1][pos]
        new_horses = []
        best_time = float("inf")

        for (time, energy, speed) in horses:
            if energy >= dist:
                new_time = time + dist / float(speed)
                new_horses.append((new_time, energy - dist, speed))
                best_time = min(best_time, new_time)

        new_horses.append((best_time, e[pos], s[pos]))  # Adds new horse
        horses = new_horses

    return str(best_time)

line = -1
with open(input) as f:
    f_out = open(output, 'w')
    lines = f.readlines()

    def read_line():
        global line
        line += 1
        # print(lines[line])
        return lines[line]

    t = int(read_line())

    for i in range(1, t+1):
        print("Case %d out of %d" % (i, t))

        n, q = map(int, read_line().split())

        e = []
        s = []
        for _ in range(n):
            e_i, s_i = map(int, read_line().split())
            e.append(e_i)
            s.append(s_i)

        d = []
        for __ in range(n):
            d.append(list(map(int, read_line().split())))

        u = []
        v = []
        for ___ in range(q):
            u_k, v_k = map(int, read_line().split())
            u.append(u_k)
            v.append(v_k)

        f_out.write("Case #%d: %s\n" % (i, solve(n, q, e, s, d, u, v)))