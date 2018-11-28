
cases = int(raw_input())

for i in range(cases):
    line = raw_input()
    shyest, rest = line.split()
    needed = 0
    people_so_far = 0

    for index, each in enumerate(list(rest)):
        c = int(each)

        if index > people_so_far:
            needed += 1
            people_so_far += 1

        people_so_far += c

    print 'Case #%d: %d' %(i + 1, needed)
