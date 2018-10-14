#!/usr/bin/python2.7

import sys


# aud is a list of ints
def calc_friends(aud):
    # print "audience: %s" % aud
    friends = 0
    size = 0
    level = 0
    for k in aud:
        friends_old = friends
        # print "k: %s" % k
        if (size+friends) <= level and level is not 0:
            friends += level - (size + friends)
        # print "friends added: %s" % (friends - friends_old)
        # print "current audience size: %s" % size
        size += k
        level += 1

    # print "Friends needed: %d" % friends
    return max(friends, 0)


input_filename = sys.argv[1]
output_filename = input_filename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')


#lines is a list of lines of the file
num_cases = int(input_file.readline())
lines = input_file.readlines()

for case in range(0, len(lines)):
    audience_input = lines[case]
    audience = []
    for c in audience_input[2:-1]:
        # print "input '%s'" % c
        if c:
            audience.append(int(c))

    output_file.write("Case #" + str(case+1) + ": " + str(calc_friends(audience)) + "\n")

print "doei"

input_file.close()
output_file.close()
