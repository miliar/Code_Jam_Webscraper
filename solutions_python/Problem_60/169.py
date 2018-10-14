
from sys import argv

def in_time(distance, speed, time):
    return time * speed >= distance


with open(argv[1]) as input:
    c = int(input.readline().strip())

    for case in xrange(1, c+1):
        n, k, b, t = [int(x) for x in input.readline().strip().split(' ')]
        positions = [int(x) for x in input.readline().strip().split(' ')]
        speeds = [int(x) for x in input.readline().strip().split(' ')]
        k = int(k)

        chicks = []
        fast_enough = 0
        for idx, pos in enumerate(positions):
            will_make_it = in_time(b-pos, speeds[idx], t)
            chicks.append(will_make_it)
            if will_make_it:
                fast_enough += 1

        if fast_enough < k:
            print "Case #%s: %s" % (case, "IMPOSSIBLE")
        elif k == 0:
            print "Case #%s: 0" % (case)
        else:
            steps = 0
            while not all(chicks[-k:]):
                for i, tmp in reversed(list(enumerate(chicks[:-k]))):
                    if tmp == True: break
                if not chicks[i+1]:
                    chicks[i+1], chicks[i] = chicks[i], chicks[i+1]
                    steps += 1
                else:
                    for i, tmp in reversed(list(enumerate(chicks))):
                        if not tmp and chicks[i-1]: 
                            chicks[i-1], chicks[i] = chicks[i], chicks[i-1]
                            steps += 1
                            break
                
            print "Case #%s: %s" % (case, steps)

