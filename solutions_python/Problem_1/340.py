import sys;


class Problem:
    def __init__(self, search_engines):
        self.S = len(search_engines)
        self.searches = dict(zip(search_engines, range(self.S)))
        self.switches = 0

    def get_index(self, q):
        return self.searches[q]

    def solve(self, questions):
        self.Q = len(questions)
        m = [self.process_request(q) for q in questions]
        s = self.get_switches(m, 0);
        if s > 0:
            s = s-1
        return s

    def get_switches(self, m, j):
        if j >= self.Q:
            return 0
        else:
            k = self.get_max_path_len(m, j)
            return 1 + self.get_switches(m, j+k)
    

    def get_max_path_len(self, m, j):
        return max([self.path_len(m, j, i) for i in range(self.S)])

    def path_len(self, m, j, i):
        count = 0
        for a in range(j, self.Q):
            if m[a][i] == 0:
                count = count + 1
            else:
                return count
        return count


    def process_request(self, q):
        i = self.get_index(q)
        new = [0] * self.S
        new[i] = 1
        return new


def parse_input(f):
    n = int(f.readline())
    return (read_test_case(f) for i in range(n))

def read_test_case(f):
    n = int(f.readline())
    searches = [f.readline() for i in range(n)]
    m = int(f.readline())
    queries = [f.readline() for i in range(m)]
    return (searches, queries)


def print_result(i, r):
    print 'Case #%d: %s' % (i, r)



if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    input = parse_input(sys.stdin)
    n = 0
    for tc in input:
        p = Problem(tc[0])
        r = p.solve(tc[1])
        n = n+1
        print_result(n, r)
