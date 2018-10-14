
import sys
sys.setrecursionlimit(2000)
# Saving the Universe

class ML:
    def __init__(self, li, n):
        self.queries = li 
        self. n = n

    # Given a list of numbers, each number in 1 to n
    # We need to find the furthest occuring number. 
    # And then repeat the process.
    def ml(self, left):
        # print "Left is ", left
        if left > len(self.queries):
            return 0

        max = 0
        for i in range(1, self.n+1):
            try :
                pos = self.queries.index(i, left)
            except ValueError:
                # print i, " was not found"
                return 0

            if pos > max:
                max = pos
        
        return 1+self.ml(max)
                


if __name__ == '__main__':
    cases = int(raw_input())

    for i in range(cases):
        nse = int(raw_input())
        ses = {}
        queries = []

        # input search engines
        # and hash them
        for j in range(1, nse+1):
            e = raw_input().strip()
            ses[e] = j

        # now take each of the queries in
        nq = int(raw_input())
        while nq:
            queries.append(ses[raw_input().strip()])
            nq-=1

        # print ses
        # print queries
        m = ML(queries, nse)

        print "Case #%d: %d"%(i+1, m.ml(0))
