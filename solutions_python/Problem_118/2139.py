import math

class Case:
    start = 0
    stop = 0
    result = 0
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop


cases = []
#open in file
fin = open("c.in", "r")
#get # of cases
numOfCases = int(fin.readline())
for line in fin.readlines():
    tmpar = line.split(" ")
    tmpcase = Case(int(tmpar[0]), int(tmpar[1]))
    cases.append(tmpcase)
#close in file
fin.close()

#calculate
for c in cases:
    squares = []
    fairs = []
    for x in range(c.start, c.stop+1):
        y = math.sqrt(x)
        if y % 1 == 0:
            squares.append(x)
        if str(x) == (str(x)[::-1]):
            fairs.append(x)
    intersection = list(set(squares) & set(fairs))
    for x in intersection:
        y = int(math.sqrt(x))
        if str(y) != (str(y)[::-1]):
            intersection.remove(x)
    c.result = len(intersection)

#open out file
fout = open("c.out", "w")
for i,c in enumerate(cases):
    fout.write("Case #"+str(i+1)+": "+str(c.result)+"\n")
