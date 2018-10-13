f = open("B-large.in")
strings = f.readlines()
f.close()

NumberTestCases = int(strings[0])
strings.pop(0)

normalDict = {
'0':'0 0 0',
'1':'0 0 1',
'2':'0 1 1',
'3':'1 1 1',
'4':'1 1 2',
'5':'2 2 1',
'6':'2 2 2',
'7':'2 2 3',
'8':'3 3 2',
'9':'3 3 3',
'10':'3 3 4',
'11':'3 4 4',
'12':'4 4 4',
'13':'4 4 5',
'14':'4 5 5',
'15':'5 5 5',
'16':'5 5 6',
'17':'5 6 6',
'18':'6 6 6',
'19':'6 6 7',
'20':'7 7 6',
'21':'7 7 7',
'22':'8 7 7',
'23':'8 8 7',
'24':'8 8 8',
'25':'9 8 8',
'26':'9 9 8',
'27':'9 9 9',
'28':'9 9 10',
'29':'10 10 9',
'30':'10 10 10'
}            

suprisesDict = {
'0':'0 0 0',
'1':'0 0 0',
'2':'0 0 2',
'3':'0 1 2',
'4':'0 2 2',
'5':'1 1 3',
'6':'2 3 1',
'7':'3 3 1',
'8':'4 2 2',
'9':'4 3 2',
'10':'4 4 2',
'11':'5 3 3',
'12':'3 4 5',
'13':'5 5 3',
'14':'4 4 6',
'15':'4 6 5',
'16':'6 6 4',
'17':'5 5 7',
'18':'7 6 5',
'19':'7 7 5',
'20':'6 6 8',
'21':'6 7 8',
'22':'6 8 8',
'23':'9 7 7',
'24':'9 8 7',
'25':'9 9 7',
'26':'8 8 10',
'27':'10 9 8',
'28':'10 10 8',
'29':'10 10 9', #copied from normal
'30':'0 0 0'
}      

caseNumber = 1
Output=open("googlersOutput.txt","w") 
for string in strings:
    googlers = 0
    str = string.split(' ')
    NumberDancers = int(str[0])
    suprises = int(str[1])
    bestResult = int(str[2])
    str.pop(0)
    str.pop(0)
    str.pop(0)
    
    words = str[-1]
    str[-1] = words[:-1]

    for points in str:
        if(suprises == 0):
            sequence = normalDict[points].split(' ')
            for number in sequence:
                if(int(number) >= bestResult):
                    googlers += 1
                    break
        elif(suprises > 0):
            complete = False
            sequence = normalDict[points].split(' ')
            supriseSequence = suprisesDict[points].split(' ')
            for number in sequence:
                if(int(number) >= bestResult):
                    googlers += 1
                    complete = True
                    break
            if(complete == True):
                continue
            for numeral in supriseSequence:
                if(int(numeral) >= bestResult):
                    googlers += 1
                    suprises -= 1
            
    suprisesDone = False
    alreadyRegistered = False;
    if(suprises != 0):
        for points in str:
            suprisesSequence = suprisesDict[points].split(' ')
            for character in suprisesSequence:
                if(int(character) >= bestResult):
                    suprises -= 1
                    if(suprises == 0):
                        suprisesDone = True
                        break
            if(suprisesDone == True):
                break
    
    noBestResult = False
    containsBestResult = False
    if(suprises != 0):
        for points in str:
            if(suprises != 0):
                suprisesSequence = suprisesDict[points].split(' ')
                for character in suprisesSequence:
                    if(int(character) < bestResult):
                        noBestResult = True
                    else:
                        containsBestResult = True
                        noBestResult = False
                if(noBestResult == True):
                    if(suprises == 0):
                        break   
                    else:
                        if((containsBestResult == False) and (googlers > 0) and (noBestResult == False)):
                            googlers -= 1
                        suprises -= 1        

    print("Case #%d: %d"%(caseNumber, googlers,))
    Output.write("Case #%d: %d\n"%(caseNumber, googlers,))
    caseNumber += 1

Output.close()