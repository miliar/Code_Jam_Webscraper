import sys

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)
    
    def readline(self):
        return [int(x) for x in self.fp.readline().split()]

def gcd(a, b):
    if a > b:
        return gcd(b, a)
    elif a == b:
        return a
    elif a == 0:
        return b
    else:
        return gcd(b % a, a)

def gcd_list(l):
    assert l
    result = l[0]
    for x in l[1:]:
        result = gcd(result, x)
    return result

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    cases, = reader.readline()
    for case in range(cases):
        r, k, n = reader.readline()
        groups = reader.readline()
        assert n == len(groups)

        perm = [None] * n
        car_sizes = [None] * n
        for i in range(n):
            j = i
            first = True
            car_size = 0
            while (first or j != i):
                first = False
                if car_size + groups[j] > k:
                    break
                else:
                    car_size += groups[j]
                    j = (j + 1) % n
            car_sizes[i] = car_size
            perm[i] = j

        # figure out orbit and orbit offset
        path = [None] * n
        line_pos = 0
        i = 0
        while True:
            if path[line_pos] is not None:
                orbit_offset = path[line_pos]
                orbit_start = line_pos
                period = i - path[line_pos]
                break
            path[line_pos] = i
            i += 1
            line_pos = perm[line_pos]

        # figure out how much money is made during orbit
        orbit_money = 0
        first = True
        line_pos = orbit_start
        while first or line_pos != orbit_start:
            first = False
            orbit_money += car_sizes[line_pos]
            line_pos = perm[line_pos]

        # figure out money up to orbit (or less if necessary)
        money = 0
        line_pos = 0
        for i in xrange(min(r, orbit_offset)):
            money += car_sizes[line_pos]
            line_pos = perm[line_pos]
        if r > orbit_offset:
            assert line_pos == orbit_start
            orbit_count, leftover = divmod(r - orbit_offset, period)
            money += orbit_count * orbit_money
            for i in xrange(leftover):
                money += car_sizes[line_pos]
                line_pos = perm[line_pos]

        print "Case #%d: %s" % (case + 1, money)
