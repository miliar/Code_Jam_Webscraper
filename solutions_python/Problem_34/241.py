"""
Kamal Wood
Tuesday, 2 September 2009
Google Code Jam 2009
Qualification Round
A. Alien Language
"""

class Letter:
    def __init__(self, val):
        self.val = val

    def checkLetter(self, letter):
        if letter in self.val:
            return True
        return False


class Word:
    def __init__(self, string):
        self.letters = []

        loc = 0
        while loc < len(string):
            char = string[loc]
            if char == '(':
                temp = ""
                loc += 1
                while string[loc] != ')':
                    temp = temp + string[loc]
                    loc += 1
                char = temp
            self.letters.append(Letter(char))
            loc += 1

##    def addLetter(self, string):
##        self.letters.append(Letter(char))

    def checkWord(self, word):
        if len(word) != len(self.letters):
            return False

        loc = 0
        while loc < len(word):
            if not self.letters[loc].checkLetter(word[loc]):
                return False
            loc += 1
        return True

def main():
    outFile = open("A-large-output.out","w")
    with open("A-large.in","r") as inFile:
        line = inFile.readline()
        line = line.split()

        wordLength = int(line[0])
        numKnownWords = int(line[1])
        totalCases = int(line[2])
        N = 1

        knownWords = []
        while numKnownWords > 0:
            line = inFile.readline()
            knownWords.append(line)
            numKnownWords -= 1

        while N <= totalCases:
            answer = 0
            line = inFile.readline()

            word = Word(line)

            for thing in knownWords:
                if word.checkWord(thing):
                    answer += 1

            outFile.write("Case #%d: %d\n" %(N, answer))
            N += 1

    outFile.close()

main()