if __name__ == '__main__':
    fo = open("1.out", "w")
    fi = open("1.in", "r")
    T = int(fi.readline())
    for tt in range(T):
        (d, m) = [int(x) for x in fi.readline().split(' ')]
        horse = [[int(x) for x in fi.readline().split(' ')] for i in range(m)]
        maxspeed = 100000000000000.0
        for i in range(m):
            for j in range(m):
                if i != j:
                    if horse[i][0] < horse[j][0] and horse[i][1] > horse[j][1]:
                        t = (horse[j][0] - horse[i][0]) / float(horse[i][1] - horse[j][1])
                        p = t * horse[i][1] + horse[i][0]
                        if p <= d:
                            maxspeed = maxspeed if maxspeed < p / t else p / t
        for i in range(m):
            if horse[i][0] < d:
                t = (d - horse[i][0]) / float(horse[i][1])
                maxspeed = maxspeed if maxspeed < d / t else d / t
        fo.write('Case #{0}: {1:.6f}\n'.format(tt + 1, maxspeed))
