__author__ = 'Constantine-pc'

with open('tmp', 'r') as f:
    d = f.readlines()

test_case_number = int(d[0])
data = []
for i in xrange(test_case_number):
    max_level, s = d[i+1].split(' ')
    max_level = int(max_level)

    standup_number = 0
    friends_num = 0
    for index, c in enumerate(s[:-1]):
        if c != '0':
            if standup_number < index:
                friends_num += (index-standup_number)
            standup_number += (int(c) + friends_num)

    data.append(friends_num)

with open('out', 'w') as out:
    for i, v in enumerate(data):
        if i == len(data):
            out.write("Case #%d: %d" % (i+1, v))
        out.write("Case #%d: %d\n" % (i+1, v))