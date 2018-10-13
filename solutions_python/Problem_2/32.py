from sys import stdin

def str_to_min(s):
    h, m = s.split(':')
    return 60 * int(h) + int(m)

class Train(object):
    def __init__(self, departure, arrival):
        self.departure = departure
        self.arrival = arrival
        self.start = True
        self.turned = False

    def try_to_turn(self, other, turnaround):
        if other.start and not self.turned and \
               other.departure >= self.arrival + turnaround:
            other.start = False
            self.turned = True

N = int(stdin.readline())

for n in range(1, N+1):
    turnaround = int(stdin.readline())
    NA, NB = [int(x) for x in stdin.readline().split()]
    train_AB = []
    for na in range(NA):
        d, a = [str_to_min(s) for s in stdin.readline().split()]
        train_AB.append(Train(d, a))
    train_BA = []
    for nb in range(NB):
        d, a = [str_to_min(s) for s in stdin.readline().split()]
        train_BA.append(Train(d, a))

    train_AB.sort(lambda x, y: cmp(x.arrival, y.arrival))
    train_BA.sort(lambda x, y: cmp(x.departure, y.departure))
    for t_AB in train_AB:
        for t_BA in train_BA:
            t_AB.try_to_turn(t_BA, turnaround)

    train_AB.sort(lambda x, y: cmp(x.departure, y.departure))
    train_BA.sort(lambda x, y: cmp(x.arrival, y.arrival))
    for t_BA in train_BA:
        for t_AB in train_AB:
            t_BA.try_to_turn(t_AB, turnaround)

    start_AB = sum(t.start for t in train_AB)
    start_BA = sum(t.start for t in train_BA)
    print 'Case #%d: %d %d' % (n, start_AB, start_BA)
    
