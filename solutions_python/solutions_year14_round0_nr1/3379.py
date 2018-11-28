import sys


class Case(object):

    def __init__(self, n, stream):
        self._id = n
        self._stream = stream

    def getNextSet(self):
        n = int(f.readline())
        for _l in xrange(1, 5):
            line = f.readline()
            if _l == n:
                answer = set(line.split())

        return answer

    def solve(self):
        first_set = self.getNextSet()
        second_set = self.getNextSet()

        result = first_set.intersection(second_set)
        size = len(result)
        if size == 0:
            self.report("Volunteer cheated!")
        elif size > 1:
            self.report("Bad magician!")
        else:
            self.report(list(result)[0])

    def report(self, msg):
        print "Case #%d: %s" % (self._id, msg)

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    t = int(f.readline())
    for _t in xrange(1, t+1):
        c = Case(_t, f)
        c.solve()
