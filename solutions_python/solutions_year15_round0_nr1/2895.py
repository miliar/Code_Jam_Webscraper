f = open('A-large.in', 'r')
case_count = f.readline()
for case in range(int(case_count)):
    ovation_max, values = f.readline().strip().split(" ")
    count = 0
    to_add = 0

    for index, value in enumerate(values):
        if count + to_add >= ovation_max:
            break

        if count + to_add < index:
            to_add += index - (count + to_add)

        count += int(value)

    print 'Case #%d: %d' % (case + 1, to_add)
