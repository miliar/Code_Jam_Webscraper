import sys

    
num_cases = int(sys.stdin.readline())
f = open('myfile','w')

for n in range(0, num_cases):
    board1guess = int(sys.stdin.readline()) - 1

    board1 = []
    for i in range(0,4):
        line = sys.stdin.readline()
        board1.append(line.split())
 
    board2guess = int(sys.stdin.readline()) - 1
    board2 = []
    for i in range(0,4):
        line = sys.stdin.readline()
        board2.append(line.split())
    
    num_same = 0

    for i in board2[board2guess]:
        for j in board1[board1guess]:
            if i == j:
                match = i
                num_same += 1

    if num_same == 1:
        f.write("Case #" + str(n+1) + ": " + str(match) + "\n")
    elif num_same > 1:
        f.write("Case #" + str(n+1) + ": Bad magician!\n")
    else:
        f.write("Case #" + str(n+1) + ": Volunteer cheated!\n")
f.close()

