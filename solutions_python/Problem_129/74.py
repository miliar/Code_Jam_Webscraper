import sys

def rstr():
    return sys.stdin.readline().strip()

def rarray():
    return rstr().split()

def rint():
    return int(rstr())

def rcase():
    N, M  = map(int, rarray())
    tickets = [map(int, rarray()) for _ in range(M)]
    return N, M, tickets

def solve(case):
    N, M, tickets = case
    passange_source = {}
    passange_sink = {}
    stops = set()
    for oi, ei, pi in tickets:
        passange_sink.setdefault(ei, []).append(pi)
        passange_source.setdefault(oi, []).append(pi)
        stops.add(oi)
        stops.add(ei)
    current_tickets = []
    total = 0
    allstop = sorted(list(stops))
    for i in allstop:

        if i in passange_source:
            current_tickets.append((i, sum(passange_source[i])))

        if i in passange_sink:

            # try to use the most recently tickets
            tmp = sum(passange_sink[i])
            while tmp > 0:
                nearest = current_tickets.pop(-1)

                if nearest[1] >= tmp:
                    d = i - nearest[0]
                    total += tmp*(2*N - d + 1)*d/2
                    if nearest[1] > tmp:
                        current_tickets.append((nearest[0], nearest[1]-tmp))

                    break
                else:
                    d = i - nearest[0]
                    total += nearest[1]*(2*N-d+1)*d/2
                    tmp -= nearest[1]

    realtotal = sum(pi*(2*N - (ei-si) + 1)*(ei-si)/2 for si, ei, pi in tickets)
    return (realtotal-total)%1000002013

T = rint()
for i in range(1, T+1):
    case = rcase()
    print "Case #%d: %d" % (i, solve(case))

