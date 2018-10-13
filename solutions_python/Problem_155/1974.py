import sys

for i, line in enumerate(sys.stdin):
    if i > 0:
        max_shy, shy_scores = line.strip().split()
        num_friends = 0
        num_standing = 0
        for j, s in enumerate(shy_scores):
            if (num_standing + num_friends) < j and int(s):
                num_friends += j - (num_standing + num_friends)
            num_standing += int(s)
        print 'Case #%d: %d' % (i, num_friends)
