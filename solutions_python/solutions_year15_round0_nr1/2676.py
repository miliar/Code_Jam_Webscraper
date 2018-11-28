
f = open('test.txt')
T = int(f.readline())

for i in range(1, T+1):
    (max_s, peoples) = f.readline().split(' ')

    needed_freinds = 0
    shyness_level = 0

    for j in range(0, int(max_s)+1):
        current_shy_people = int(peoples[j])

        # print "current_shy_people = ", current_shy_people, " shyness_level = ", shyness_level
        if j > shyness_level:
            needed_freinds += j - shyness_level
            shyness_level = j

        shyness_level += current_shy_people

    print "Case #%s: %s" % (i, needed_freinds)
