import sys

filename = sys.argv[1]
fd = open(filename)
lines = [l.strip() for l in fd.readlines()]
fd.close()

T = int(lines[0])

for case in range(1, T+1):
    people = lines[case].split()[1]
    invites = 0
    people_accum = 0
    for i in range(0, len(people)):
        invites += i - people_accum - invites
        people_accum += int(people[i])
    print "Case #%d: %d" % (case, invites)

