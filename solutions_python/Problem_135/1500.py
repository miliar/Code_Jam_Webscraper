
import sys

questions = int(sys.stdin.readline())

for q in xrange(questions):
    firstA = int(sys.stdin.readline())
    firstBoard = []
    firstBoard.append(sys.stdin.readline().strip().split(' ')) 
    firstBoard.append(sys.stdin.readline().strip().split(' ')) 
    firstBoard.append(sys.stdin.readline().strip().split(' ')) 
    firstBoard.append(sys.stdin.readline().strip().split(' ')) 

    secondA = int(sys.stdin.readline())
    secondBoard = []
    secondBoard.append(sys.stdin.readline().strip().split(' ')) 
    secondBoard.append(sys.stdin.readline().strip().split(' ')) 
    secondBoard.append(sys.stdin.readline().strip().split(' ')) 
    secondBoard.append(sys.stdin.readline().strip().split(' ')) 

    inters = (set(firstBoard[firstA-1]) & set(secondBoard[secondA-1]))

    case = "Case #%d: " % (q+1)
    if len(inters) == 1:
        print case + str(inters.pop())
    elif len(inters) > 1:
        print case + "Bad magician!"
    else:
        print case + "Volunteer cheated!"
