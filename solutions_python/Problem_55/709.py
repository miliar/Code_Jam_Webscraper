import os, sys

data = open(sys.argv[1], "r")
inputs = int(data.readline())

for i in xrange(inputs):
    r, k, n = [int(x) for x in data.readline().split()]
    queue = [int(x) for x in data.readline().split()]
    money = 0
    for ride in xrange(r):
        post_queue = []
        groups = 0
        while len(queue) > 0:
            if (groups + queue[0]) > k:
                break
            group = queue.pop(0)
            post_queue.append(group)
            groups += group
        money += groups
        queue.extend(post_queue)
    print "Case #%d: %d" % (i + 1, money)
