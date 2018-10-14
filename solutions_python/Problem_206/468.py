is_from_file = False

class Horse:
    def __init__(self, p, s):
        self.p = p
        self.s = s

    def get_min_v(self, d):
        return self.p * self.s / float(d - self.p) + self.s


def solve(d, n, horses):
    return min([horse.get_min_v(d) for horse in horses])


if is_from_file:
    f = open('demo.in')
    # f = open('A-small-attempt0.in')
    for t in range(1, int(f.readline()) + 1):
        d, n = map(int, f.readline().split())
        horses = []
        for i in range(n):
            k, s = map(int, f.readline().split())
            horse = Horse(k, s)
            horses.append(horse)
        v = solve(d, n, horses)

        print 'Case #%d: %f' % (t, v)
else:
    for t in range(1, int(raw_input()) + 1):
        d, n = map(int, raw_input().split())
        horses = []
        for i in range(n):
            k, s = map(int, raw_input().split())
            horse = Horse(k, s)
            horses.append(horse)
        v = solve(d, n, horses)

        print 'Case #%d: %f' % (t, v)
