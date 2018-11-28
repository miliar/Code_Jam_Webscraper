out = open('A-large.out', 'w')

with open('A-large.in', 'r') as f:
    lines = f.readlines()
lim = int(lines[0])

for i in range(1, lim + 1):
    smax, people = lines[i].split()
    people_standing = 0
    need_to_invite = 0
    for s, p in enumerate(people):
        if p == '0':
            continue
        if people_standing >= s:
            people_standing += int(p)
        else:
            diff = s - people_standing
            need_to_invite += diff
            people_standing += diff + int(p)
        if s >= int(smax):
            break
    # print "Case #%d: %d" % (i, need_to_invite)
    out.write("Case #%d: %d\n" % (i, need_to_invite))
out.close()
