import sys
import datetime
from sets import Set

class Train:
    def __init__(self, s, n, dt):
        self.s = s
        self.n = n
        self.dt = dt

    def set_dt(self, dt):
        self.dt = dt

    def finished(self, t):
        return self.dt[1] == t

    def __str__(self):
        return '<%s %i %s>' % (self.s, self.n, self.dt)

    def __repr__(self):
        return '<%s %i %s>' % (self.s, self.n, self.dt)


class Station:
    def __init__(self, id, timetable):
        self.id = id
        self.table = timetable
        self.free = []
        self.in_use = []
        self.max_number = 0

    def process1(self, t, s):
        free = [n for n in self.in_use if n.finished(t)]
        for z in free:
            self.in_use.remove(z)

        s.put_free(free)
        
    def process2(self, t, s):
        start = [dt for dt in self.table if dt[0] == t]
        for x in start:
            if self.free:
                self.reuse_free(x)
            else:
                self.create_new(x)
                
    def reuse_free(self, dt):
        n = self.free.pop()
        n.set_dt(dt)
        self.in_use.append(n)


    def create_new(self, dt):
        self.max_number = self.max_number + 1
        n = Train(self.id, self.max_number, dt)
        self.in_use.append(n)
            

    def get_max(self):
        return self.max_number

    def put_free(self, free):
        self.free.extend(free)

    def __str__(self):
        return '<%s %i %s %s>' % (self.id, self.max_number, self.free, self.in_use)

class Problem:

    def solve(self, timetable):
        timeline = []
        for d in self.flatten(timetable):
            timeline.append(d[0])
            timeline.append(d[1])

        # remove duplicates
        s = Set(timeline)
        timeline = [i for i in s]
        timeline.sort()

        sa = Station('A', timetable[0])
        sb = Station('B', timetable[1])

        for t in timeline:
            sa.process1(t, sb)
            sb.process1(t, sa)
            sa.process2(t, sb)
            sb.process2(t, sa)

        return (sa.get_max(), sb.get_max())


    def flatten(self, t):
        r = t[0][:]
        r.extend(t[1][:])
        return r


def parse_input(f):
    n = int(f.readline())
    return (read_test_case(f) for i in range(n))


def read_test_case(f):
    T = int(f.readline())
    n = f.readline().split()
    ta = [parse_duration(f.readline()) for i in range(int(n[0]))]
    tb = [parse_duration(f.readline()) for i in range(int(n[1]))]
    return ([shift_time(t, T) for t in ta],
            [shift_time(t, T) for t in tb])

def shift_time(t, delta):
    z = delta + t[1].minute
    h = z / 60
    m = z % 60
    new_h = h + t[1].hour
    if new_h > 23:
        new_h = 23
    return (t[0], datetime.time(new_h, m))

def parse_duration(s):
    a = s.split()
    return (parse_time(a[0]), parse_time(a[1]))

def parse_time(s):
    t = s.split(':')
    return datetime.time(int(t[0]), int(t[1]))


def print_result(i, r):
    print 'Case #%d: %i %i' % (i, r[0], r[1])


if __name__ == '__main__':
    input = parse_input(sys.stdin)
    n = 0
    for tc in input:
        p = Problem()
        r = p.solve(tc)
        n = n+1
        print_result(n, r)
