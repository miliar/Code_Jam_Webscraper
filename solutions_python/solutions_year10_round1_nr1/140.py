import re
from math import floor

#fileName = "input.txt"
#fileName = "A-small-attempt2.in"
fileName = "A-large.in"
input = open(fileName)
outputFile = open("output-large.txt", "w")

def readLine(stream=input):
    return stream.readline().replace("\r","").replace("\n","")
    
def writeLine(text):
    outputFile.write(str(text).lstrip().rstrip() + "\n")
    print text
    
T = int(readLine())
for caseIndex in xrange(T):
    N,K = map(lambda x: int(x), readLine(input).split(" "))
    blueWin,redWin=False,False
    board = []
    for i in range(N):
        row = readLine(input)
        row = row.replace('.','')
        row = '.'*(N-len(row)) + row
        board.append(row)
    
    rPat,bPat = "R.{%d}","B.{%d}"
    rAcross = re.compile('.*' + 'R'*K)
    bAcross = re.compile('.*' + 'B'*K)
    
    rDown = re.compile('.*' + (rPat%(N,))*(K-1)+"R")
    bDown = re.compile('.*' + (bPat%(N,))*(K-1)+"B")
    
    rUpDiag = re.compile('.*' + (rPat%(N+1,))*(K-1)+"R")
    bUpDiag = re.compile('.*' + (bPat%(N+1,))*(K-1)+"B")
    
    rDownDiag = re.compile('.*' + (rPat%(N-1,))*(K-1)+"R")
    bDownDiag = re.compile('.*' + (bPat%(N-1,))*(K-1)+"B")
    
    concat = "X".join(board)
    
    if rAcross.match(concat) or rDown.match(concat) or rUpDiag.match(concat) or rDownDiag.match(concat):
        redWin = True
        
    if bAcross.match(concat) or bDown.match(concat) or bUpDiag.match(concat) or bDownDiag.match(concat):
        blueWin = True
    
        
    if blueWin and redWin:
        result = "Both"
    elif blueWin:
        result = "Blue"
    elif redWin:
        result = "Red"
    else:
        result = "Neither"
    writeLine("Case #%d: %s" % (caseIndex+1,result))
    