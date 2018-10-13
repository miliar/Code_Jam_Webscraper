#Things to do:
#First check if there are any winners
#when checking if there are winners make a note of empty states
#has to accept the file as an input and the output must be in the specified format

class tic_tomek:

    def __init__(self, inFile):
        self.inFile = open(str(inFile),'r')
        self.cases = self.inFile.readline()
        self.test = []
        self.output = ''
        self.testLine = ''
    
    def get_next_case(self):
        """Gets the next 4 lines which correspond to the next test case"""
        self.test = []
        for i in range(4):
            self.test.append(self.inFile.readline().strip('\n'))
        self.inFile.readline() #removes the blank line after each case
    
    def check_winner(self):
        self.output = ''
        if 'T' in self.testLine:
            if self.testLine.count('X') == 3:
                self.output = 'X won'
                return
            elif self.testLine.count('O') == 3:
                self.output = 'O won'
                return
        else:
            if self.testLine.count('X') == 4:
                self.output = 'X won'
                return
            
            elif self.testLine.count('O') == 4:
                self.output = 'O won'
                return

    def solve_case(self):
        self.testLine = ''
        for i in range(4): #checks the row of each case
            self.testLine = self.test[i]
            self.check_winner()
            if self.output != '':
                return
        self.testLine = ''
        #next bit checks each column
        for i in range(4):
            self.testLine = ''
            for j in range(4):
                self.testLine += self.test[j][i]
            self.check_winner()
            if self.output != '':
                return
        self.testLine = ''
        for i in range(4):
            self.testLine += self.test[i][i]
            self.check_winner()
        if self.output != '':
            return
        self.testLine = ''
        for i in range(4):
            self.testLine += self.test[i][3 - i]
        self.check_winner()
        if self.output != '':
            return
                


        num_dot = 0
        for i in range(4):
            num_dot += self.test[i].count('.')
        
        if num_dot != 0:
            self.output = 'Game has not completed'
        else:
            self.output = 'Draw'
    
    def solve_le_cases(self):
        op_file = raw_input('File to store result in : ')
        op_file = open(op_file,'w')
        num_solved = 1 
        while num_solved < self.cases :
            opLine = 'Case #'
            num_solved = num_solved + 1
            self.get_next_case()
            if '' in self.test:
                return
            self.solve_case()
            opLine = opLine + str(num_solved - 1) + ': ' + self.output + '\n'
            print opLine,
            op_file.write(opLine)



file_name = raw_input('File name(with .in extension) :',)
tic_tac = tic_tomek(file_name)
tic_tac.solve_le_cases()
