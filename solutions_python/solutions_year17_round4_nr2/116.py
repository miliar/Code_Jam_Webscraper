import math

T = int(input())
for i in range(1, T + 1):
    [N, C, M] = [int(x) for x in input().split(" ")]
    tickets = []
    for j in range(M):
        tickets.append([int(x) for x in input().split(" ")])
    tickets.sort()

    places = []
    for j in range(N):
        places.append([])
    for t in tickets:
        places[t[0]-1].append(t[1])


    minimum = 0
    for j in range(1, N+1):
        subtrain = places[:j]
        if len(subtrain[-1]) == 0:
            continue
        for b in range(1, C+1):
            minimum = max(sum(x.count(b) for x in subtrain), minimum)

        minimum = max(math.ceil(sum(len(x) for x in subtrain) / j), minimum)

    moves = 0
    for place in places:
        if len(place) > minimum:
            moves += len(place) - minimum

    print("Case #{}: {} {}".format(i, minimum, moves))
