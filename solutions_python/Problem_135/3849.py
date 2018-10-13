def operation(x,s1,s2):
    file = open('magician-output-small.txt','a')
    s = s1 & s2
    if(len(s) >= 1):
        if(len(s) == 1):
            file.write("Case #%d: %d\n" %(x,s.pop()))
        else:
            file.write("Case #%d: Bad magician!\n" % x)
    else:
        file.write("Case #%d: Volunteer cheated!\n" % x)
    file.close()
        
def check(answer):
    for y in range(4):
        matrixRow  = file.readline().split(" ")
        if(answer == y+1):
            matrixRow = list(map(int,matrixRow))
            sets = set(matrixRow)
    return(sets)
            

file = open('magician-input-small.txt','r+')
case = int(file.readline())
for x in range(case):
    answer = int(file.readline())
    setOne = check(answer)
    answer = int(file.readline())
    setTwo = check(answer)
    operation(x+1,setOne,setTwo)
file.close()
