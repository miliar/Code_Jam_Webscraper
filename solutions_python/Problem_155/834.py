fi = open("A-large.in", 'r')
fo = open("A-large-out.txt", 'w')

T = int(fi.readline())
for case in xrange(1, T + 1):
    line = fi.readline().split()
    smax, audience = int(line[0]), line[1]

    # go over audience, keeping count of how many you need to add at each level to get them standing
    standing = int(audience[0]) # 0 shyness: already standing
    extra = 0

    for i in xrange(1, smax + 1):
        # need to add extra?
        if standing < i:
            diff = i - standing
            standing += diff
            extra += diff
        standing += int(audience[i])

    fo.write("Case #{}: {}\n".format(case, extra))

fi.close()
fo.close()
