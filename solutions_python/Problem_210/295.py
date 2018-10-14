f = open('B-small-attempt1.in')
fw = open('B-small.out', 'w')

T = int(f.readline())
for t in xrange(T):
    Ac, Aj = map(int, f.readline().split())
    Ac_list = []
    Aj_list = []
    for i in xrange(Ac):
        start, end = map(int, f.readline().split())
        Ac_list.append((start, end))
    for i in xrange(Aj):
        start, end = map(int, f.readline().split())
        Aj_list.append((start, end))
    Ac_list.sort()
    Aj_list.sort()
    if Ac + Aj <= 1:
        ans = 2
    elif Ac == 1 and Aj == 1:
        ans = 2
    elif Ac == 2:
        if Ac_list[1][1] - Ac_list[0][0] <= 720 or Ac_list[0][1] + 1440 - Ac_list[1][0] <= 720:
            ans = 2
        else:
            ans = 4
    elif Aj == 2:
        if Aj_list[1][1] - Aj_list[0][0] <= 720 or Aj_list[0][1] + 1440 - Aj_list[1][0] <= 720:
            ans = 2
        else:
            ans = 4
    else:
        ans = 0
    fw.write('Case #' + str(t + 1) + ': ' + str(ans) + '\n')

fw.close()
f.close()
