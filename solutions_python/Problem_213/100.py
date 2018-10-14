import sys
stdin = sys.stdin
ncases = int(stdin.readline())

class Train:
    def __init__(self, n):
        self.pos = [None for i in range(n)]
        self.uniq = set()

    def add(self, b, p):
        self.pos[p] = b
        self.uniq.add(b)

    def add_pos(self, b, p):
        if b in self.uniq:
            return None
        for i in range(p, -1, -1):
            # print("trying {0}({1}) in {2}: {3}".format(b, p, i, self.pos[i]))
            if self.pos[i] is None:
                return i


for ncase in range(ncases):
    N, C, M = map(int, stdin.readline().strip().split(' '))

    tickets = []
    ticketsPerC = {}
    ticketsAtPos = {}
    for i in range(M):
        P, B = map(int, stdin.readline().strip().split(' '))
        P = P - 1
        if B not in ticketsPerC:
            ticketsPerC[B] = []
        ticketsPerC[B].append(P)
        tickets.append((P, B))

        if P not in ticketsAtPos:
            ticketsAtPos[P] = 0
        ticketsAtPos[P] += 1

    if ncase == 10:
        print(N, C, M, file=sys.stderr)
        for t in tickets:
            print(t[0] + 1, t[1], file=sys.stderr)


    tickets = list(sorted(tickets))
    c_by_len = list(sorted(ticketsPerC.items(), key=lambda a:len(a[1])))

    def attempt(x):
        trains = []
        npromote = 0

        # for p, b in tickets:
        sort_fn = lambda a: a

        for b, ps in c_by_len:
            for p in sorted(ps, key=sort_fn):
                min_p = None
                min_t = None
                min_cost = None
                for t in trains:
                    p2 = t.add_pos(b, p)
                    if p2 is None: continue
                    cost = 0 if p2 == p else 1
                    if min_t is None or cost < min_cost:
                        min_p = p2
                        min_t = t
                        min_cost = cost
                    if cost == 0:
                        break

                if min_t is None:
                    min_t = Train(N)
                    min_p = p
                    min_cost = 0
                    trains.append(min_t)

                min_t.add(b, min_p)
                npromote += min_cost

            if x == 1:
                sort_fn = lambda a: -a #ticketsAtPos[a]
        return len(trains), npromote
    
    res = min(attempt(0), attempt(1))

    print('Case #{0}: {1} {2}'.format(ncase + 1, res[0], res[1]))