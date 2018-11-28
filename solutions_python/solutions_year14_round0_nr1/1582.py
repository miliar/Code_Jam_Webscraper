myfile = open("A-small-attempt0.in.txt", "r")
output = open("output.txt", "w")

cases = int(myfile.readline().strip())
case = 0

while case < cases:
    line1 = 0
    line2 = 0
    board1 = []
    board2 = []
    firstRow = int(myfile.readline().strip())-1
    while line1< 4:
        board1.append(myfile.readline().split())
        line1 += 1
    firstGuess = board1[firstRow]
   
    
    secondRow = int(myfile.readline())-1
    while line2 < 4:
        board2.append(myfile.readline().split())
        line2 += 1
        
    same = []
    secondGuess = board2[secondRow]
    for num in firstGuess:
        if num in secondGuess:
            same.append(num)
    answer = ""
    if len(same) == 0:
        answer = "Volunteer cheated!"
    elif len(same) == 1:
        answer = same[0]
    else:
        answer  = "Bad magician!"
 
    output.write("Case #"+ str(case+1) + ": " + answer + "\n")
    case += 1

myfile.close()
output.close()

