import sys
import math
import time
class Case(object):

    def __init__(self, case, start, end):
        self.case = case
        self.start = start
        self.end = end
        
    def get_count(self):
        start_sqrt = int(math.ceil(math.sqrt(self.start)))
        end_sqrt = int(math.floor(math.sqrt(self.end)))
        count = 0
        i = start_sqrt
        while i <= end_sqrt:
            if self.is_palin(i):
                ii = i*i
                if self.is_palin(ii):
                    count += 1
            i += 1
        return count
            
    def is_palin(self, nbr):
        nbrstr = str(nbr)
        n = len(nbrstr)
        for j in range(n / 2):
            if not nbrstr[j] == nbrstr[n-1-j]:
                return False
        return True
        
def read_input(stream): 
    line1 = stream.readline()
    number_of_cases = int(line1.strip())
    for i in range(number_of_cases):
        start, end = [int(x) for x in stream.readline().strip().split()]
        yield Case(i+1, start, end)
    
        
if __name__ == '__main__':
    for x in read_input(sys.stdin):
        print 'Case #{0}: {1}'.format(x.case, x.get_count())
        