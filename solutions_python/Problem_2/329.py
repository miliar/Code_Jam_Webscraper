import re

in_file = open('b.in')

test_cases = int(in_file.readline())

def read_time(side):
    h1, m1, h2, m2 = (int(x) for x in re.match('(\d+):(\d+) (\d+):(\d+)', in_file.readline()).groups())
    return h1*60+m1, h2*60+m2, side

for test_case in range(1, test_cases+1):
    turnaround_time = int(in_file.readline())
    na, nb = (int(x) for x in re.match('(\d+) (\d+)', in_file.readline()).groups())

    tt = []
    w = [[], []] # waiting trains
    c = [0, 0]   # trains need to start

    for i in range(na):
        tt.append(read_time(0))

    for i in range(nb):
        tt.append(read_time(1))

    tt.sort()

    # t = [start, arrive, starting_side]

    for t in tt:
        # no train waiting at all
        if not w[t[2]]:
            c[t[2]] += 1
        else:
            q = min(w[t[2]])

            if q <= t[0]:
                w[t[2]].remove(q)
            else:
                c[t[2]] += 1

        w[1-t[2]].append(t[1]+turnaround_time)

    print "Case #%d: %d %d" % (test_case, c[0], c[1])
