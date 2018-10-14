import numpy as np

with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def count_speed(d, horses):
    d = float(d)
    if len(horses) == 1:
        horse = horses[0]
        t = (d - horse[0]) / horse[1]
        return d / t
    else:
        horses = sorted(horses, key=lambda x: x[0])
        print horses
        t = 0
        while len(horses) > 1:
            h1 = horses[0]
            h2 = horses[1]
            if h2[1] == h1[1]:
                x = -1000000000000
            else:
                x = (h1[0] * h2[1] - h2[0] * h1[1]) / (h2[1] - h1[1])
            print x
            print h1[0]
            print h2[0]
            if x < min(h1[0], h2[0]) or x > d:
                print 'horses do not meet'
            else:
                horses[0] = (x, min(h1[1], h2[1]))
                t += (x - h1[0]) / h1[1]
            del horses[1]
            print 'time', t
            print 'horses left', horses

        horse = horses[0]
        t_last = (d - horse[0]) / horse[1]
        print 'last horse', horse
        print 'time', t_last
        return d / (t + t_last)


f = open('out.txt', 'w')
line_count = 1
i = 1
while True:
    try:
        d, n = lines[line_count].split(' ')
        line_count += 1
        d = int(d)
        n = int(n)
        print d, n
        horses = []
        for j in xrange(line_count, line_count + n):
            ki, si = lines[j].split(' ')
            line_count += 1
            ki = int(ki)
            si = int(si)
            print ki, si
            horses.append((ki, si))
        speed = count_speed(d, horses)
        print('Case #%s: %f \n' % (i, speed))
        f.write('Case #%s: %f \n' % (i, speed))
        i += 1
        print '-----------------'
    except:
        break
f.close()
