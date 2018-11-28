SET_NAME = 'A-large'

def solve_case(infile):
    N, K = map(int, infile.readline().split())
    data = []
    for i in xrange(N):
        data.append(infile.readline().strip())
        
    board = Board(data)
    board.rotate()
    board.output()
    winners = board.getWinners(K)
    if len(winners) == 0:
        return 'Neither'
    elif len(winners) == 2:
        return 'Both'
    else:
        return 'Blue' if 'B' in winners else 'Red'


class Board:
    def __init__(self, data):
        self.data = data
        self.size = len(data)
            
    def rotate(self):
        '''clockwise'''
        self.push_rows()
        data_prime = []
        for i in xrange(self.size):
            data_prime.append(''.join(map(lambda row : row[i], self.data[-1::-1])))
        self.data = data_prime
            
    def push_rows(self):
        for i in xrange(self.size):
            self.data[i] = self.data[i].replace('.','')
            self.data[i] = '.'*(self.size - len(self.data[i])) + self.data[i]
            
    def output(self):
        print '\n'.join(self.data)
        
    def getWinners(self, k):
        winners = []
        winners.extend(self.getWinnersHorizontal(k))
        winners.extend(self.getWinnersVertical(k))
        winners.extend(self.getWinnersDiagDown(k))
        winners.extend(self.getWinnersDiagUp(k))
        return set(winners)
        
    def getWinnersHorizontal(self, k):
        winners = []
        for i in xrange(self.size):
            length_of_streak = 0
            start = ''
            for j in xrange(self.size):
                place = self.data[i][j]
                if place == '.':
                    start == ''
                    length_of_streak = 0
                elif place == start:
                    length_of_streak += 1
                else:
                    start = place
                    length_of_streak = 1
                if length_of_streak == k:
                    winners.append(start)
        return set(winners)
        
    def getWinnersVertical(self, k):
        winners = []
        for i in xrange(self.size):
            length_of_streak = 0
            start = ''
            for j in xrange(self.size):
                place = self.data[j][i]
                if place == '.':
                    start == ''
                    length_of_streak = 0
                elif place == start:
                    length_of_streak += 1
                else:
                    start = place
                    length_of_streak = 1
                if length_of_streak == k:
                    winners.append(start)
        return set(winners)
        
    def getWinnersDiagUp(self, k):
        winners = []
        for diag in xrange(2*self.size - 1):
            length_of_streak = 0
            start = ''
            for place in xrange(min(diag+1, 2*self.size - 1 - diag)):
                i = max(0, diag - (self.size - 1)) + place
                j = diag - i
                val = self.data[i][j]
                if val == '.':
                    start == ''
                    length_of_streak = 0
                elif val == start:
                    length_of_streak += 1
                else:
                    start = val
                    length_of_streak = 1
                if length_of_streak == k:
                    winners.append(start)
        return set(winners)
        
    def getWinnersDiagDown(self, k):
        winners = []
        for diag in xrange(2*self.size - 1):
            length_of_streak = 0
            start = ''
            for place in xrange(min(diag+1, 2*self.size - 1 - diag)):
                i = max(0, diag - (self.size - 1)) + place
                j = self.size - 1 - (diag - i)
                val = self.data[i][j]
                if val == '.':
                    start == ''
                    length_of_streak = 0
                elif val == start:
                    length_of_streak += 1
                else:
                    start = val
                    length_of_streak = 1
                if length_of_streak == k:
                    winners.append(start)
        return set(winners)

def main():
    """
    Standard main method for all google code jam problems
    """
    infile = open('%s.in'%(SET_NAME))
    outfile = open('%s.out'%(SET_NAME), 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        print 'Solving case #%d...'%(i+1)
        output = 'Case #%d: %s\n'%(i+1, solve_case(infile))
        print output
        outfile.write(output)
    outfile.close()
               
if __name__ == '__main__':
    main()