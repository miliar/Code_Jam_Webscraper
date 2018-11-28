import math
import pdb

t = int(input())

for i in range(t):
    s = input().split(" ")
    n = int(s[0])
    q = int(s[1])
    horses = []
    for _ in range(n):
        s = input().split(" ")
        endurance = int(s[0])
        speed = int(s[1])
        endurance = endurance/speed
        horses.append((endurance, speed))

    distances = []

    for _ in range(n):
        s = [int(x) for x in input().split(" ")]
        d = {}
        for k,v in enumerate(s):
            if v!=-1:
                d[k] = v
        
        distances.append(d)


    cost = [[math.inf for x in range(n)] for y in range(n)]
    to_update = []
    for j in range(n):
        cost[j][j] = 0
        to_update.append((j,j))

    while to_update:
        x, y = to_update.pop()
        for z in distances[y]:
            candidate = cost[x][y] + distances[y][z]/horses[x][1]
            
            if cost[x][z] > candidate and candidate<=horses[x][0]:
                cost[x][z] = candidate
                to_update.append((x,z))

    answers = []

    for _ in range(q):
        s = input().split(" ")
        start = int(s[0]) - 1
        end = int(s[1]) - 1

        arrival = {x:math.inf for x in range(n)}
        arrival[start]=0

        current = start
        #pdb.set_trace()


        while current!=end:
            for x in arrival:
                if arrival[x]>arrival[current]+cost[current][x]:
                    arrival[x] = arrival[current]+cost[current][x]
            arrival.pop(current)
            current = min(arrival, key=arrival.get)

        answers.append(str(arrival[end]))

    print("Case #{}: {}".format(i+1, " ".join(answers)))
