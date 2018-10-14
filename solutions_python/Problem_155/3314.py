f = open("a.in")

f.readline()

for case, line in enumerate(f):
    people = line.split()[1]

    standing = 0
    res = 0
    for shyness, count in enumerate(people):
        count = int(count)
        if (shyness <= standing):
            standing += count
        else:
            res += shyness - standing
            standing += shyness - standing + count
    print "Case #" + str(case) + ": " + str(res)
