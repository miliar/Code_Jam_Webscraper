
T = int(raw_input().strip())

for idx in range(1, T+1):
    pancakes, flips = raw_input().split()
    flips = int(flips)
    pancakes = list(pancakes)
    for i in range(len(pancakes)):
        if pancakes[i] == '+':
            pancakes[i] = True
        else:
            pancakes[i] = False

    if len(pancakes) < flips:
        if sum(pancakes) == len(pancakes):
            print "Case #%d: %d" % (idx, 0)
        else:
            print "Case #%d: IMPOSSIBLE" % (idx)
        continue

    count = 0
    for i in range(len(pancakes)-flips+1):
        if not pancakes[i]:
            count += 1
            for j in range(flips):
                pancakes[i+j] = True if pancakes[i+j] == False else False

    if sum(pancakes) == len(pancakes):
        print "Case #%d: %d" % (idx, count)
    else:
        print "Case #%d: IMPOSSIBLE" % (idx)
