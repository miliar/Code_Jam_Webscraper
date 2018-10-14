from sys import stdin


def getInts():
    return list(map(int, stdin.readline().strip().split(' ')))


def newPosition(current, nextHorse):
    start1 = current[0]
    speed1 = current[1]
    start2 = nextHorse[0]
    speed2 = nextHorse[1]
    if(len(nextHorse) == 3):
        start1 = start1 + (nextHorse[2] * speed1)
        time = (start2 - start1) / (speed1 - speed2)
        return ((start1 + (time * speed1)), time + nextHorse[2])
    else:
        time = (start2 - start1) / (speed1 - speed2)
        return ((start1 + (time * speed1)), time)


T = int(input())
for case in range(1, T+1):
    D, N = getInts()
    horses = [getInts() for x in range(0, N)]
    horses.sort()
    change = True
    while(change):
        change = False
        for x in range(0, len(horses) - 1):
            currentHorse = horses[x]
            nextHorse = horses[x+1]
            if nextHorse[1] < currentHorse[1]:
                newPos, time = newPosition(currentHorse, nextHorse)
                if(newPos < D):
                    newHorse = [newPos, nextHorse[1]]
                    newHorse.append(time)
                    horses = horses[:x] + [newHorse] + horses[x+2:]
                    horses.sort()
                    change = True
                    break;
    slowest = horses[0]
    time = slowest[2] if len(slowest) == 3 else 0
    h = D / (((D - slowest[0]) / slowest[1]) + time)
    print("Case #{}: {}".format(case, h))


