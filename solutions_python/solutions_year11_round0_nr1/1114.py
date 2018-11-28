import sys

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

def get_answer(s):
    buf= s.split(' ')
    L = zip(buf[1::2], [int(x) for x in buf[2::2]])
    current_robot = L[0][0]
    time = 0
    r_time = {}
    pos = {}
    r_time['B'] = 0
    r_time['O'] = 0
    pos['B'] = 1
    pos['O'] = 1
    for x in L:
        walk_time = abs(pos[x[0]] - x[1])
        if x[0] == current_robot:
            time += walk_time + 1
        else:
            time = (time + 1) if (time > r_time[x[0]] + walk_time) else (r_time[x[0]] + walk_time + 1)
        pos[x[0]] = x[1]
        current_robot = x[0]
        r_time[x[0]] = time
    return time

n = int(in_file.readline())
for x in xrange(n):
    s = in_file.readline()
    out_file.writelines("Case #%d: %d\n" % (x + 1, get_answer(s)))

