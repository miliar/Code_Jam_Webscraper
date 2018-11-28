T = int(raw_input().strip())

for t in range(T):
    D, N = [int(item) for item in raw_input().strip().split()]
    horses = list()
    for n in xrange(N):
        horses.append([int(item) for item in raw_input().strip().split()])
    horses.sort(key = lambda item: item[0], reverse = True)
    max_time_use = 0
    for horse in horses:
        time_use = float(D - horse[0]) / float(horse[1])
        max_time_use = max(max_time_use, time_use)
    print('Case #%d: %f' % (t +1, float(D) / max_time_use))

