fread = open('A-large.in')
lines = fread.readlines()
fw = open('output1large', 'w')

T = int(lines[0][0:-1])
i = 1
for t in range(T):
    line = lines[i].split(" ")
    i += 1
    D = int(line[0])
    N = int(line[1])

    horses = []

    for n in range(N):
        line2 = lines[i].split(" ")
        i += 1
        K = int(line2[0])
        S = int(line2[1])
        horses.append([K, S])

    horses.sort(key=lambda tup: tup[0], reverse=True)

    prev_arrival_t = 0

    for horse in horses:
        arrival_t = (D - horse[0]) / horse[1]
        if arrival_t > prev_arrival_t:
            prev_arrival_t = arrival_t

    speed = D / prev_arrival_t

    fw.write('Case #{}: {}\n'.format(t+1, speed))
