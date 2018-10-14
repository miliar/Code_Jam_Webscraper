with open ("input.in", "r") as myfile:
    problem=myfile.read()
lines = problem.split('\n')
cases = int(lines[0])

fo = open('problemA.out', 'w')
def outfile(text):
    fo.write (text+"\n")


for k in range(cases):
    index = k*10+1
    case=lines[index:index+11]
    Case1 = case[int(case[0])]
    Case2 = case[int(case[5])+5]
    Case1 = Case1.split(" ")
    Case2 = Case2.split(" ")
    numberExist = 0
    cardOrder = 0
    for i in Case1:
        for j in Case2:
            if(i==j):
                cardOrder=i
                numberExist+=1
    if(numberExist==1):
        outfile("case #"+str(k+1)+": " + cardOrder)
    elif(numberExist>1):
        outfile("case #"+str(k+1)+": Bad magician!")
    elif(numberExist==0):
        outfile("case #"+str(k+1)+": Volunteer cheated!")
fo.close()