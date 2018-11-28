#!/usr/bin/python

testcases = int(raw_input())

for i in range(testcases):
    inputline = raw_input().rstrip()
    (_, counts) = inputline.split()
    attendees = list()
    for num in counts:
        attendees.append(int(num))
    # How many people to stand up on their own?
    num_standing = 0
    friends = 0
    for shy_level in range(len(attendees)):
        if attendees[shy_level] > 0:
            diff = max(shy_level - num_standing, 0)
            friends += diff
            num_standing += diff + attendees[shy_level]

    print "Case #%d: %d" % (i+1, friends)
