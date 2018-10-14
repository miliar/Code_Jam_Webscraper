from sys import stdin

def solve(t):

    line = stdin.readline().split(' ')
    n = int(line[0])
    c = int(line[1])
    m = int(line[2])

    tickets = {}
    for i in range(0, c):
        tickets[i] = []

    for i in range(0, m):
        line = stdin.readline().split(' ')
        p = int(line[0])
        b = int(line[1]) - 1
        tickets[b].append(p)

    # if t != 27:
    #     return

    for i in range(0, c):
        tickets[i].sort()

    # print(n)
    # print(m)
    # #
    # print(tickets[0])
    # print(tickets[1])

    rides = 0
    promos = 0
    t11 = 0
    t12 = 0
    t21 = 0
    t22 = 0
    for p in tickets[1]:
        if p == 2:
            t22 += 1
        else:
            t21 += 1

    for p in tickets[0]:
        if p == 2:
            t12 += 1
        else:
            t11 += 1

    # print(str(t11) + ' ' + str(t12) + ' ' + str(t21) + ' ' + str(t22) + ' ' )

    for p in tickets[0]:
        second = -1
        for p2 in tickets[1]:
            if p2 > p:
                second = p2
                break
        if second == -1:
            for p2 in tickets[1]:
                if p2 != p:
                    second = p2
                    break
        # print('sec' + str(second))
        rides += 1
        if second != -1:
            tickets[1].remove(second)
        else:
            if tickets[1]:
                # Only same
                if p != 1:
                    promos += 1
                    tickets[1].remove(p)
        # print(tickets[1])
        # print(promos)

        # tickets[0] = tickets[0][1:]



    rides += len(tickets[1])

    assert rides <= m


    print('Case #' + str(t + 1) + ': ' + str(rides) + ' ' + str(promos))

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
