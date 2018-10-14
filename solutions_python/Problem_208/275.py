numCases = int(raw_input())

for t in range(1, numCases+1):
    nTowns, nTasks = [int(s) for s in raw_input().split()]
    horses = []
    for i in range(nTowns):
        horses.append([int(s) for s in raw_input().split()])

    towns = []
    for i in range(nTowns):
        if i != nTowns -1:
            towns.append([int(s) for s in raw_input().split()][i+1])
        else:
            raw_input()
    task = [int(s) for s in raw_input().split()]

    minTime = [-1]*nTowns
    minTime[-1] = 0

    for i in reversed(range(nTowns-1)):
        end, spd = horses[i]
        for j in range(i+1, nTowns):
            end -= towns[j-1]
            if end >= 0:
                time = minTime[j] + float(sum(towns[i:j]))/spd
                if time < minTime[i] or minTime[i] == -1:
                    minTime[i] = time
            else:
                break

    print "Case #{}: {}".format(t, minTime[0])





