from sys import argv

_, input_file = argv

output = open(input_file + '_out.txt', 'w+')

with open(input_file) as fp:
    fp.readline()

    case = 1
    for line in fp:
        line = line.strip()

        max_shyness, audience = line.split(' ')
        max_shyness = int(max_shyness)

        people = [int(p) for p in list(audience)]
        shyness = {}

        # fill it up
        for i in range(max_shyness+1):
            shyness[i] = people[i]

        # see who's missing
        people_standing = 0
        additional_people = 0
        for level, count in shyness.iteritems():
            if level == 0:
                people_standing += count
                continue

            diff = level - people_standing

            if diff > 0:
                # we need more standers
                additional_people += diff
                people_standing += diff

            people_standing += count

        out = "Case #%s: %s" % (case, additional_people)
        output.write(out + "\n")
        print out
        case += 1

output.close()