import sys

sys.setrecursionlimit(5000)

class Solver:

    def __init__(self, engines):
        self.engines = engines

    def start(self, queries):
        return min(self.search(queries, engine, 0) for engine in self.engines)

    def search(self, queries, cur_engine, length):
        if not queries:
            return length
        try:
            pivot = queries.index(cur_engine)
        except:
            return length
        length += 1
        query = queries[pivot]
        queries = queries[pivot:]
        pivots = []
        for engine in self.engines:
            if engine != query:
                try:
                    pivots.append(queries.index(engine))
                except:
                    return length
        i = max(pivots)
        return self.search(queries[i:], queries[i], length)

if __name__ == "__main__":
    for case in xrange(int(raw_input())):
        s = int(raw_input())
        engines = [raw_input() for i in xrange(s)]
        q = int(raw_input())
        queries = [raw_input() for i in xrange(q)]
        solver = Solver(engines)
        print "Case #%i: %i" % (case + 1, solver.start(queries))
