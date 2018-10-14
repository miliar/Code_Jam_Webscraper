f = open('A-large.in', 'r')
o = open('A-large.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    case_data = f.readline().strip().split()
    D = int(case_data[0])
    N = int(case_data[1])
    max_time = 0
    for i in xrange(N):
        horse_data = f.readline().strip().split()
        horse_time = (D - float(horse_data[0])) / float(horse_data[1])
        if horse_time > max_time:
            max_time = horse_time
    max_speed = float(D) / max_time
    s = "Case #%d: %f\n" % (t+1, max_speed)
    o.write(s)