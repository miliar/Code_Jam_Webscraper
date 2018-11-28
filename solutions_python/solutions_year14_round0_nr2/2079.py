"""Google Code Jam 2014

   agrelle_cookieClicker
"""
import sys, os

def main():
    checkArguments(sys.argv)
    
    x = agrelle_agrelle_cookieClicker(sys.argv[1])
    answers = x.solveCookieSets()
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

class agrelle_agrelle_cookieClicker(object):
    def __init__(self, filename = None):
        # Filename may be "None" for testing purposes
        if filename: self.cookieSets = self.readFile(filename)

    def readFile(self, filename):
        """ A file to read in the input in the specified format.
        """
        f = open(filename)
        # The first line is the amount of cookieSets
        T = int(f.readline().strip())
        # Store all cookieSets from the file in the list 'cookieSets',
        # and return the result
        cookieSets = []
        for line in f: cookieSets.append([float(each) for each in line.strip().split()])
        
        while [] in cookieSets: cookieSets.remove([])
        f.close()
        assert len(cookieSets) == T, "Too many cookieSets!\n"
        return cookieSets

    def solveCookieSets(self,):
        """ A function to solve all of the cookieSets and aggegate the answer.
        """
        answer = []
        for cookieSet in self.cookieSets: answer.append(self.solveCookieSet(cookieSet))
        return answer

    def solveCookieSet(self, cookieSet):
        """ Solve each individual cookieSet and output the appropriate result
            
            If desired, add a few doctests:
        >>> agrelle_CookieSet().solveCookieSet([30.0, 1.0, 2.0])
        1.0000000
        >>> agrelle_CookieSet().solveCookieSet([30.0, 2.0, 100.0])
        39.1666667
        >>> agrelle_CookieSet().solveCookieSet([30.50000, 3.14159, 1999.19990])
        63.9680013
        >>> agrelle_CookieSet().solveCookieSet([500.0, 4.0, 2000.0])
        526.1904762
        """
        answerNow = 0.0; answerNext = -1.0;
        cookiesNow = 0.0; cookiesNext = 0.0; cps = 2.0;
        C = cookieSet[0]; F = cookieSet[1]; X = cookieSet[2];
        i = 0; temp = 0;
        while answerNow > answerNext:
            if i > 10000000:
                print "---------STOPPING-----------"
                break
            if i > 0: temp += C / (cps - F)
            else: temp = 0.
            answerNext = answerNow
            answerNow = X / cps + temp
            answerNext = X / (cps + F) + C / cps + temp
            cps += F; i += 1;
        return answerNow

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
            message = str(answers[i])
            # Write the "Case #" and the appropriate message to the file
            # or standard output (depending on how long the answer is)
            if f: f.write('Case #' + str(i+1) + ": " + message + "\n")
            else: print 'Case #' + str(i+1) + ": " + message

if __name__ == '__main__': main()
