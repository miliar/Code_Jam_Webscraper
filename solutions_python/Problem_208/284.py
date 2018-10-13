__author__ = 'rutger'


def simple_solve(N, horses, distances):


    # results: (time, (horse))
    temp = [(distances[0] / horses[0][1], (horses[0][0] - distances[0], horses[0][1]))]

    for i in range(1, N - 1):
        # take all horses possible up to that city and calculate to city + 1
        nextDist = distances[i]
        temp2 = []
        for t in temp:
            time = t[0]
            #try new horse
            horse = horses[i]
            dist = horse[0]
            speed = horse[1]

            if dist >= nextDist:
                temp2.append((time + (nextDist / speed), (dist - nextDist, speed)))


            # try old horse
            horse = t[1]
            dist = horse[0]
            speed = horse[1]

            if dist >= nextDist:
                temp2.append((time + (nextDist / speed), (dist - nextDist, speed)))


        temp = temp2
    return sorted(temp)[0][0]









def solve():
    pass


for T in range(int(input())):
    numCity, numStops = list(map(int, input().split(' ')))
    horses = []
    for i in range(numCity):
        dist, speed = list(map(int, input().split(' ')))
        horses.append((dist, speed))

    #read graph
    distances = []
    for i in range(numCity - 1):
        dists = list(map(int, input().split(' ')))
        distances.append(dists[i + 1])
    input()

    # read destinations
    for i in range(numStops):
        input()

    res = simple_solve(numCity, horses, distances)
    print('Case #%d: %f' % (T + 1, res))