t = input()
for case_no in range(1, t+1):
    n, m = map(int, raw_input().split())
    cost = [0]
    i = n
    while i > 1:
        cost.append(cost[-1]+i)
        #print i
        i -= 1
    events = []
    actual_cost = 0
    for i in range(m):
        (o, e, p) = map(int, raw_input().split())
        actual_cost += cost[e-o]*p
        events.append((o, p))
        events.append((e,-p))
    events.sort()
    tickets = []
    cur_cost = 0
    i = 0
    while i < 2*m:
        j = i
        enter, leave = 0, 0
        while j < len(events) and events[j][0] == events[i][0]:
            if events[j][1] > 0:
                enter += events[j][1]
            else:
                leave += -events[j][1]
            j += 1
        if enter > 0:
            tickets.append((events[i][0], enter))
        while leave > 0:
            ss, np = tickets.pop()
            if leave < np:
                cur_cost += cost[events[i][0]-ss]*leave
                np -= leave
                tickets.append((ss, np))
                leave = 0
            else:
                leave -= np
                cur_cost += cost[events[i][0]-ss]*np
        i = j
    #print actual_cost, cur_cost
    print 'Case #%d: %d' % (case_no, actual_cost - cur_cost)