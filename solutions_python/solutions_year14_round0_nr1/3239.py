txtlist = [i.strip() for i in open('asmall.txt').readlines()]
#print txtlist

numberofCases = int(txtlist[0])
output = open('magicout','w')
cases = []
startindex = 1
for i in range(numberofCases):
    cases.append(txtlist[startindex:startindex+10])
    startindex +=10    

for i in range(numberofCases):
    targetrow1 = int(cases[i][0])
    grid1 = [x.split() for x in cases[i][1:5]]
    targetrow2 = int(cases[i][5])
    grid2 = [x.split() for x in cases[i][6:11]]
    count = 0
    result = 0   
    for item in grid1[targetrow1 -1 ]:
        if item in grid2[targetrow2 - 1]:
            count+=1
            result = item
    if count == 1:
        outstring = str(result)
    elif count == 0:
        outstring = 'Volunteer cheated!'
    else:
        outstring = 'Bad magician!'
    output.write('Case #'+ str(i+1)+': '+outstring+'\n')
    print 'Case #'+ str(i+1)+': '+outstring+'\n'
    

#def solver(case):
    
