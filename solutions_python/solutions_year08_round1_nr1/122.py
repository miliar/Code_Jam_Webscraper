



class case(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def solve(self):
        self.v1.sort()
        self.v2.sort(reverse=True)

        return sum([self.v1[i] * self.v2[i] for i in xrange(len(self.v1))])

    @staticmethod
    def readcase():
        input()     # skip size line
        v1 =  map(int, raw_input().split())
        v2 =  map(int, raw_input().split())
        return case(v1, v2)

    def print_solution(self, caseno):
        print 'Case #%d: %d' % (caseno, self.solve())


#
# main code
#

input()     # skip no of cases line
CaseNo = 1
try:
    while True:
        case.readcase().print_solution(CaseNo)
        CaseNo += 1
except EOFError:
    pass

    
