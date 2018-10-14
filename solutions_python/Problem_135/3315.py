txt = [line.strip() for line in open('input.txt').readlines()]
numberofCases = int(txt[0])
output = open('output.txt','w')
caseList = []
startIndex = 1

for case in range(numberofCases):
    caseList.append(txt[startIndex:startIndex+10])
    startIndex +=10    

for index in range(numberofCases):
    row_A = int(caseList[index][0])
    cardLayout_A = [line.split() for line in caseList[index][1:5]]
    row_B = int(caseList[index][5])
    cardLayout_B = [line.split() for line in caseList[index][6:11]]
    count = 0
    result = 0   
    for card in cardLayout_A[row_A -1 ]:
        if card in cardLayout_B[row_B - 1]:
            count+=1
            result = card
    if count == 1:
        ans = str(result)
    elif count == 0:
        ans = 'Volunteer cheated!'
    else:
        ans = 'Bad magician!'
    output.write('Case #'+ str(index+1)+': '+ans+'\n')
    
