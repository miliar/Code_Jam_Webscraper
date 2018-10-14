
if __name__ == '__main__':
    t = int(raw_input())
    for t in xrange(1, t + 1):
        min_num = 0
        ac, aj = map(int, raw_input().split(' '))
        activities_c = []
        for i in xrange(ac):
            activities_c.append(map(int, raw_input().split(' ')))
        activities_c.sort(key=lambda x: (x[0]))
        # print activities_c

        activities_j = []
        for i in xrange(aj):
            activities_j.append(map(int, raw_input().split(' ')))
        activities_j.sort(key=lambda x: (x[0]))
        # print activities_j

        # small dataset has only 5 cases
        min_num = 2
        if len(activities_c) > 1:
            if min(activities_c[-1][1] - activities_c[0][0], (24*60 - activities_c[-1][0]) + activities_c[0][1]) > 720:
                min_num = 4
        elif len(activities_j) > 1:
            if min(activities_j[-1][1] - activities_j[0][0], (24*60 - activities_j[-1][0]) + activities_j[0][1]) > 720:
                min_num = 4

        print "Case #%d: %d" % (t, min_num)
