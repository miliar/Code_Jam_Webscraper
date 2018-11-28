from sys import stdin

testcases = int(stdin.readline())

for case in xrange(testcases):
    
    c, d = map(int, stdin.readline().strip().split(" "))

    positions = []

    max_move = 0
    groups = []
    
    for _ in xrange(c):
        p, v = map(int, stdin.readline().strip().split(" "))

        group_move = (v-1)*d/2.0
        groups.append((p-group_move, p+group_move, group_move))
    looping = True
    while looping:
        looping = False
        group = groups[0]
        new_groups = []
        for new_group in groups[1:]:
            overlap = group[1] - new_group[0] + d
            if overlap > 0:
                # Overlap
                looping = True
                if group[2] - new_group[2] > overlap:
                    group = (group[0], new_group[1] + overlap, group[2])
                elif new_group[2] - group[2] > overlap:
                    group = (group[0] - overlap, new_group[1], new_group[2])
                else:
                    new_move = (group[2] + new_group[2] + overlap) / 2
                    group = (group[0] - (new_move - group[2]),
                             new_group[1] + (new_move - new_group[2]),       
                             new_move)
            else:
                new_groups.append(group)
                group = new_group
        new_groups.append(group)
        groups = new_groups
    for group in groups:
        if group[2] > max_move:
            max_move = group[2]

    print("Case #%d: %f" % (case+1,max_move))
