T = int(raw_input())

for t in xrange(T):
    first_ans = int(raw_input()) - 1
    first_arr = []
    for i in range(0, 4):
        first_arr.append(raw_input().split())

    second_ans = int(raw_input()) - 1
    second_arr = []
    for i in range(0, 4):
        second_arr.append(raw_input().split())

    possible = []
    for item in first_arr[first_ans]:
        if item in second_arr[second_ans]:
            possible.append(item)

    if len(possible) == 1:
        print "Case #%s: %s" % (t+1, possible[0])
    elif len(possible) == 0:
        print "Case #%s: Volunteer cheated!" % (t+1,)
    else:
        print "Case #%s: Bad magician!" % (t+1,)
