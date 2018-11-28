from heapq import heappush


def calc_speed(h, dest):
    tmax = 0.00
    for j in reversed(h):
        time_to_dest = (dest - j[0]) / j[1]
        if time_to_dest > tmax:
            tmax = time_to_dest
    return dest / tmax

f = open('dataset.txt')
out = open('output.txt', 'w')

cases = int(f.readline())

for i in range(cases):
    [dest, horses] = f.readline().split(' ')
    dest = int(dest)
    horses = int(horses)

    horseq = []
    
    for j in range(horses):
        [pos, speed] = f.readline().split(' ')
        pos = int(pos)
        speed = int(speed)

        heappush(horseq, (pos, speed))

    print('Case #{}: {}'.format(i + 1, calc_speed(horseq, dest)), file=out)
