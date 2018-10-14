import sys, os

in_path = sys.argv[1]

if not os.path.exists(in_path):
    raise ValueError("%s doesn't exist!" % in_path)

fd = open(in_path, 'rt')
out_fd = open(in_path.split('.')[0] + '.out', 'wt')

line = fd.readline().strip()
test_cases = int(line)

# import ipdb
# ipdb.set_trace()

for case in xrange(1, test_cases + 1):
    line = fd.readline().split()
    s_max = int(line[0])
    containers = [int(el) for el in line[1]]
    leftover = 0
    friends_needed = 0

    for idx in xrange(0, len(containers) - 1):
        if containers[idx] > 0:
            leftover += containers[idx] - 1
        else:
            if leftover > 0:
                leftover -= 1
            else:
                friends_needed += 1

    out_fd.write("Case #%d: %d\n" % (case, friends_needed))

fd.close()
out_fd.close()