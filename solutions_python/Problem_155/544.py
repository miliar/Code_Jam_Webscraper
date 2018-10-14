data = open("input/problema.txt")
nb_cases = int(data.readline())

for z in xrange(nb_cases):
    print "Case #%d:" % (z + 1),
    line = data.readline().rstrip('\n').split(" ")
    s_max = int(line[0])
    s = [int(x) for x in line[1]]
    # print s_max, s
    prev = 0
    total = 0
    for i in xrange(s_max + 1):
        if prev >= i:
            prev += s[i]
        if prev < i:
            to_add = i - prev
            prev += to_add + s[i]
            total += to_add
    print total
