import collections

class Coaster(object):
    def __init__(self):
        self.capacity = 0
        self.groups = []
        
    def get_people_count(self):
        return sum(self.groups)
        
    def load(self, queue):
        groups = self.groups
        people_count = self.get_people_count()
        while queue and (queue[-1] <= self.capacity - people_count):
            group = queue.pop()
            groups.append(group)
            people_count += group
            

def calc_profit(coaster, ride_count, queue):
    profit = 0
    while ride_count > 0:
        coaster.load(queue)
        profit += coaster.get_people_count()
        queue.extendleft(coaster.groups)
        coaster.groups = []
        ride_count -= 1
    return profit

def main(input, output):
    case_count = int(input.readline())
    for i in xrange(case_count):
        coaster = Coaster()
        ride_count, coaster.capacity, group_count = map(int, input.readline().strip().split())
        groups = map(int, input.readline().strip().split())
        assert len(groups) == group_count
        queue = collections.deque(reversed(groups))
        profit = calc_profit(coaster, ride_count, queue)
        print >> output, 'Case #%d: %d' % (i+1, profit)
        
    
if __name__ == '__main__':
    import sys
    main(open(sys.argv[1]), sys.stdout)