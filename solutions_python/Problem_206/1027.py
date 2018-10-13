from operator import itemgetter

output = []
t = int(input())

for x in range(0, t):
    d, n = [int(i) for i in input().split()]
    horses = []
    for y in range(0, n):
        horses.append([int(i) for i in input().split()])
    
    horses.sort(key=itemgetter(0))

    maxtime = 0
    for horse in horses:
        dist = d - horse[0]
        time = dist / horse[1]
        if time > maxtime: maxtime = time

    output.append(d / maxtime)

for line, index in zip(output, range(1, len(output) + 1)):
    print('Case #{}: {}'.format(index, line))