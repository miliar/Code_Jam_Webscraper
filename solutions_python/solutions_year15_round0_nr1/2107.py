#!/usr/bin/env python

import sys

file = open(sys.argv[1])
next(file) # Ignore the line because this is python

lineno = 1
for line in file:
    line = line.strip()
    people, shyness = line.split()

    # Cast them all to INTs
    people = int(people) + 1
    shyness = map(int, list(shyness))
    friends_to_bring = 0
    people_applauding = 0

    # Each row needs shyness_level people to stand up
    for shyness_level in xrange(people):

        # If the sum of people applauding plus the number
        # of friends we asked isn't enough to make this row
        # applaud, we need to bring X friends more
        if people_applauding + friends_to_bring < shyness_level:
            friends_to_bring += shyness_level - (people_applauding + friends_to_bring)

        # Shy people now applaud and help us
        people_applauding += shyness[shyness_level]
    print "Case #%d: %d" % (lineno, friends_to_bring)
    lineno += 1
