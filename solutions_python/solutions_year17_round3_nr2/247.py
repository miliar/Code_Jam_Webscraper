import copy
T = int(raw_input())

for t in xrange(T):
    Ac, Aj = map(int, raw_input().split())

    Acl, Ajl = [], []
    Acd, Ajd = dict(), dict()
    AA = []
    dur = [0, 0]
    for i in xrange(Ac):
        s, e = map(int, raw_input().split())
        Acl.append((s,e))
        dur[0] += e-s
        Acd[s] = e
        AA.append(s)

    for i in xrange(Aj):
        s, e = map(int, raw_input().split())
        Ajl.append((s,e))
        dur[1] += e-s
        Ajd[s] = e
        AA.append(s)

    AA = list(sorted(AA))
    wca = [[], []] # will change anyway
    mnc = [[], []] # may not change


    prev = -100
    prev_e = -100
    for s in AA:
        new = 0 if s in Acd else 1
        duration = s - prev_e
        if prev == -100:
            prev_e = Acd[s] if s in Acd else Ajd[s]
            prev = new
            continue
        if new == prev:
            mnc[prev].append(duration)
            dur[prev] += duration
        else:
            wca[prev].append(duration)

        prev_e = Acd[s] if s in Acd else Ajd[s]
        prev = new

    # loop case
    s = AA[0]
    s_mod = s + 1440
    new = 0 if s in Acd else 1
    duration = s_mod - prev_e
    if new == prev:
        mnc[prev].append(duration)
        dur[prev] += duration
    else:
        wca[prev].append(duration)

    prev_e = Acd[s] if s in Acd else Ajd[s]
    prev = new

    # 
    # print 'bleh: ', mnc
    start_state = dur[0]
    actions = map(lambda(x): - x, mnc[0]) + mnc[1]
    free_slots = sum(wca[0]) + sum(wca[1])

    # print 'prob: ', start_state, actions
    # Dee Pee
    shortest_dist = [1000000] * 1441
    for x in range(max(0, 720-free_slots), min(1440, 720+free_slots+1)):
        shortest_dist[x] = 0
    for A in actions:
        nnn = copy.deepcopy(shortest_dist)
        if A >= 0: L = range(0, A+1)
        else: L = range(A, 1)


        for k in xrange(1441):
            for a in L:
                if k - a <= 1440 and k - a >= 0:
                    nnn[k-a] = min(nnn[k-a], shortest_dist[k] + 2)
        shortest_dist = nnn

    print 'Case #%d: %d' % (t+1, shortest_dist[start_state] + len(wca[0]) + len(wca[1]))
