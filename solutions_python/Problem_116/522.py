import re
from operator import itemgetter

class Board(object):
    def __init__(self, file_iter=None):
        if not file_iter:
            raise ValueError        
        self.read_board(file_iter)
        self.check_result()        
    def read_board(self, file_iter):
        self.square = []
        while len(self.square)<4:
            line = file_iter.next()
            line_square = re.findall(r"X|O|T|\.",line)
            if line_square:
                self.square += [line_square]
    def check_result(self):
        self.result = ''
        self.check_X_won()
        if not self.result:
            self.check_O_won()
        if not self.result:
            self.check_not_completed()
        if not self.result:
            self.result = "Draw"
    def check_X_won(self):
        #Horizontal
        for line in self.square:
            if len(re.findall(r"X|T",''.join(line))) == 4:
                self.result = "X won"
                return
        #Vertical        
        for line in zip(*self.square):
            if len(re.findall(r"X|T",''.join(line))) == 4:
                self.result = "X won"
                return
        #Diagonals
        matrix = sum(self.square,[])
        diagonal = [itemgetter(0,5,10,15)(matrix), itemgetter(3,6,9,12)(matrix)]
        for i in range(2):
            if len(re.findall(r"X|T",''.join(diagonal[i]))) == 4:
                self.result = "X won"
                return
    def check_O_won(self):
        #Horizontal
        for line in self.square:
            if len(re.findall(r"O|T",''.join(line))) == 4:
                self.result = "O won"
                return
        #Horizontal
        for line in zip(*self.square):
            if len(re.findall(r"O|T",''.join(line))) == 4:
                self.result = "O won"
                return
        #Diagonals
        matrix = sum(self.square,[])
        diagonal = [itemgetter(0,5,10,15)(matrix), itemgetter(3,6,9,12)(matrix)]
        for i in range(2):
            if len(re.findall(r"O|T",''.join(diagonal[i]))) == 4:
                self.result = "O won"
                return    
    def check_not_completed(self):
        for line in self.square:
            if re.findall(r"\.",''.join(line)):
                self.result = "Game has not completed"
                return
    
#Reading the input file
with open("A-large.in", 'r') as file:
    file_iter = iter(file.readline,'')  #filedata = file.read()
    boards = []
    try:
    	while True:        
            line = file_iter.next()
            found_number = re.search(r"\d+",line)
            if found_number:
                N = int(found_number.group(0))
                boards = [Board(file_iter) for i in range(N)]
                break
    except (StopIteration, ValueError):
        print len(boards)
        pass

#Preparing the output data
output = '\n'.join(['Case #{0}: {1}'.format(n+1,board.result) for n,board in enumerate(boards)])
#output = []
#for n,board in enumerate(boards):
#    output += 'Case #{0}: {1} \n'.format(n,board.result)

#Writing the output file
with open("filename.out", 'w') as file:
    file.write(output)