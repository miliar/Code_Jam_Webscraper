
from sys import argv


def uniq_dirs(path):
    parts = path.split('/')[1:]
    return ['/'.join(x) for x in (parts[:y+1] for y in xrange(len(parts)))]


with open(argv[1]) as input:
    t = int(input.readline().strip())

    for case in xrange(1, t+1):
        n, m = [int(x) for x in input.readline().strip().split(' ')]
        original = [input.readline().strip()[1:] for i in xrange(n)]
        newlist = set(original)
        for to_create in [input.readline().strip() for i in xrange(m)]:
            newlist.update(uniq_dirs(to_create))

        print "Case #%s: %s" % (case, len(newlist) - len(original))

