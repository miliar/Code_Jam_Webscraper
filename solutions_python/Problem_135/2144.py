"""Google Code Jam 2013 Practice

   agrelle_magicTrick
"""
import sys, os

def main():
    checkArguments(sys.argv)
    
    x = agrelle_agrelle_magicTrick(sys.argv[1])
    answers = x.solveBoards()
    x.printOutput(answers)

def checkArguments(argv):

    if len(argv) < 2: 
        print "\nToo few arguments"
        sys.exit()
    elif len(argv) > 2: 
        print "\nToo many arguments"
        sys.exit()
    elif not os.path.isfile(argv[1]):
        print "Not a valid file: " + argv[1]
        sys.exit()

class agrelle_agrelle_magicTrick(object):
    def __init__(self, filename = None):
        # Filename may be "None" for testing purposes
        if filename: self.boards = self.readFile(filename)

    def readFile(self, filename):
        """ A file to read in the input in the specified format.
        """
        f = open(filename)
        # The first line is the amount of boards
        T = int(f.readline().strip())
        # Store all boards from the file in the list 'boards',
        # and return the result
        boards = [[]]
        for line in f:
            if len(line.strip()) == 1:
                if len(boards) == 0: boards.append([int(line.strip()),[]])
                elif len(boards[-1]) == 2: boards.append([[int(line.strip()),[]]])
                else: boards[-1].append([int(line.strip()),[]])
            else:
                boards[-1][-1][-1].append([int(each) for each in line.strip().split()])
        
        while [] in boards: boards.remove([])
        f.close()
        assert len(boards) == T, "Too many boards!\n"
        return boards

    def solveBoards(self,):
        """ A function to solve all of the boards and aggegate the answer.
        """
        answer = []
        for board in self.boards: answer.append(self.solveBoard(board))
        return answer

    def solveBoard(self, board):
        """ Solve each individual board and output the appropriate result
        """
        items = []; answer = [];
        items += board[0][1][board[0][0]-1]
        items += board[1][1][board[1][0]-1]
        
        for item in items:
            if items.count(item) == 2: 
                if item not in answer: answer.append(item)
        return answer

    def printOutput(self, answers):
        """ The function to print the output in the specified format
            for all of the answers.
            
            The format will consist of:
            Case #N: [message]
            
            ... where each case N will be identified, followed by the
            appropriate message.
        """
        # If the answer is really long, open a file for output instead of printing
        # it to the screen.
        if len(answers) > 10: f = open(sys.argv[1].rsplit(".",1)[0] + ".out","w")
        else: f = None
        
        # Loop over all of the answers
        for i in range(len(answers)): 
            # Define what the 'message' will be
            if len(answers[i]) == 1: message = str(answers[i][0])
            elif len(answers[i]) > 1: message = "Bad magician!"
            else: message = "Volunteer cheated!"
            # Write the "Case #" and the appropriate message to the file
            # or standard output (depending on how long the answer is)
            if f: f.write('Case #' + str(i+1) + ": " + message + "\n")
            else: print 'Case #' + str(i+1) + ": " + message

if __name__ == '__main__': main()
