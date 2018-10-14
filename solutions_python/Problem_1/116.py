
class Problem(object):

    def __init__(self, queries, engines):
        self.queries = queries
        self.engines = engines
        # print 'INIT:', self.engines, self.queries
        
    def solve(self):
        if len(self.queries) == 0:
            return 0
        
        matrix = {}

        lastIndex = len(self.queries)-1
        matrix[lastIndex] = {}
        for engine in self.engines:
            if self.queries[lastIndex] == engine:
                matrix[lastIndex][engine] = 99999
            else:
                matrix[lastIndex][engine] = 0
            
        for queryIndex in reversed(range(len(self.queries)-1)):
            matrix[queryIndex] = {}
            for engine in self.engines:
                if self.queries[queryIndex] == engine:
                    matrix[queryIndex][engine] = 99999
                    continue

                # 1. switching
                matrix[queryIndex][engine] = 1 + min(
                    [matrix[queryIndex+1][nextEngine]
                     for nextEngine in self.engines
                     if nextEngine !=  engine])
                
                # 2. not switching 
                if True or self.queries[queryIndex] != engine:
                    matrix[queryIndex][engine] = min(
                        matrix[queryIndex][engine],
                        matrix[queryIndex+1][engine])
                    


        #self.pretty_print(matrix)
        return min([matrix[0][e] for e in self.engines])

    def pretty_print(self, matrix):
        keys = matrix.keys()
        keys.sort()
        for key in keys:
            print '%d %25s %s' % (key, self.queries[key], matrix[key])

if __name__ == '__main__':

    nr_cases = int(raw_input())
    for case_no in range(nr_cases):
        nr_engines = int(raw_input())
        engines = [raw_input() for x in range(nr_engines)]
        nr_queries = int(raw_input())
        queries = [raw_input() for x in range(nr_queries)]
        problem = Problem(queries, engines)
        print "Case #%d: %d" % (case_no+1, problem.solve())
        
