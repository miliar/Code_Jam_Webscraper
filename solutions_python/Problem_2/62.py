from_a = 1
from_b = 2
from_both = from_a | from_b

def other_dir(dir):
    return dir ^ from_both


class Trip:
    def __init__(self, line, dir):
        s, e = line.split(' ')
        sh, sm = s.split(':')
        eh, em = e.split(':')
        self.start = int(sh) * 60 + int(sm)
        self.end = int(eh) * 60 + int(em)
        self.dir = dir
        self.next = None


def first_trip(trips, start_time, dir):
    for t in trips:
        if t.start >= start_time and t.dir & dir:
            return t
    else:
        return None

        
def start_train_count(trips, start_time, T):
    a_count = b_count = 0

    while trips:
        first = first_trip(trips, start_time, from_both)
        if first.dir == from_a:
            a_count += 1
        else:
            b_count += 1
        
        last = first
        while last:
            trips.remove(last)
            last = first_trip(trips, last.end + T, other_dir(last.dir))

    return a_count, b_count

        
def cmp_start(a, b):
    return a.start - b.start


if __name__ == '__main__':
    N = input()

    for n in range(N):
        trips = []
        T = input()
        NA, NB = map(lambda s: int(s), raw_input().split(' '))
        for i in range(NA):
            trips.append(Trip(raw_input(), from_a))
        for i in range(NB):
            trips.append(Trip(raw_input(), from_b))
        trips.sort(cmp_start)

        a_count, b_count = start_train_count(trips, 0, T)
        print "Case #%d: %d %d" % (n + 1, a_count, b_count)
        
        
        
        
