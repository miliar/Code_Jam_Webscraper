__author__ = 'udi'

import sys


def check_case(firstAnswer,firstBoard,secondAnswer,secondBoard):
    assert isinstance(firstAnswer,int)
    assert isinstance(firstBoard,list)
    suspects = set()
    for num in firstBoard[firstAnswer-1]:
        suspects.add(num)
    suspects2 = set()
    for num in secondBoard[secondAnswer-1]:
        suspects2.add(num)
    return suspects.intersection(suspects2)

f = open(sys.argv[1])
T = int(f.readline())
for i in range(1,T+1):
    firstAnswer = int(f.readline())
    firstBoard = []
    for j in range(1,5):
        row = f.readline()
        row = row.split()
        firstBoard.append(row)
    secondAnswer = int(f.readline())
    secondBoard = []
    for j in range(1,5):
        row = f.readline()
        row = row.split()
        secondBoard.append(row)
    solution = check_case(firstAnswer,firstBoard,secondAnswer,secondBoard)
    assert isinstance(solution,set)
    if (len(solution)==0):
        print "Case #"+str(i)+": Volunteer cheated!"
    elif(len(solution)>1):
        print "Case #"+str(i)+": Bad magician!"
    elif(len(solution)==1):
        result = str(solution.pop())
        print "Case #"+str(i)+": "+ result