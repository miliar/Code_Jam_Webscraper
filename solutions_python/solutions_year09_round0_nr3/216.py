"""
Kamal Wood
Tuesday, 2 September 2009
Google Code Jam 2009
Qualification Round
C. Welcome to Code Jam
"""

class Letter:
    def __init__(self, val, pos):
        self.val = val # Letter's character value.
        self.pos = pos # Letter's position in the string.

class String:
    def __init__(self, string):
        self.length = len(string)

        pos = 0
        self.string = []
        while pos < self.length:
            self.string.append(Letter(string[pos], pos))
            pos += 1

        self.phrase = "welcome to code jam"
        self.phrLen = len(self.phrase)
        self.count = 0

    def countRecur(self, letter, ind):
        if self.count >= 9999:
            return
        if letter.val != self.phrase[ind]:
            return
        if ind == self.phrLen - 1:
            self.count += 1
            return
        loc = letter.pos + 1
        while loc < self.length:
            self.countRecur(self.string[loc], ind + 1)
            loc += 1

    def countMain(self):
        ind = 0
        for letter in self.string:
            self.countRecur(letter, 0)

def main():
    phrase = "welcome to code jam"
    outFile = open("C-small-attempt0-OUTPUT.out","w")
    with open("C-small-attempt0.in","r") as inFile:
        N = 1
        totalCases = int(inFile.readline())

        while N <= totalCases:
            string = String(inFile.readline())
            string.countMain()
            outFile.write("Case #%d: %4.4d\n" %(N, string.count))
            N += 1

    outFile.close()

main()