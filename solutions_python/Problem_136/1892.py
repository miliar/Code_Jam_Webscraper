INITIAL_RATE = 2


class Case(object):
    def __init__(self,C,F,X):
        self.C = C
        self.F = F
        self.X = X

    def solve(self):
        time = self.X/INITIAL_RATE
        return self.__solve_in_loop(INITIAL_RATE, time,0)
    
    def __solve_in_loop(self,last_rate,last_time,overhead):
        while (True):
            time_to_farm = self.C/last_rate + overhead
            new_rate = last_rate + self.F
            new_time = time_to_farm + self.X/new_rate
            if new_time >= last_time:
                return last_time
            last_time = new_time
            last_rate = new_rate
            overhead = time_to_farm

def parse_stdin():
    n = int(raw_input())
    cases = []
    for i in xrange(n):
        c = [float(x) for x in raw_input().split(' ')]
        cases.append(Case(c[0],c[1],c[2]))
    return cases


def main():
    cases = parse_stdin()
    i = 1
    for c in cases:
        print 'Case #{:d}: {:3.7f}'.format(i, c.solve())
        i += 1


if __name__ == '__main__':
    main()
