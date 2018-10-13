import sys

def makeRowInt(line) :
    #print ("makeRowInt")    
    eachRow = line.split()
    #print ("original eachRow : ",eachRow)
    eachRowInt = [int(x) for x in eachRow]
    #print ("Int eachRowInt : ",eachRowInt)
    return eachRowInt


#print ("start program")
txt = "A-small-attempt1.in"

infile = open(txt,'r')
count = 0
set = 0

caseCount = 0
sPla = ''
LastString = ''
for line in infile :
    if count == 0 :
                lCase = line.split()
                #print ("lCase  ------------------------- : ",lCase)
                sCase = lCase[0]
                numCase = int(sCase)
                #print ("numCase ------------------------ : ",numCase)
    if count >= 1 :
                lineCharacter = count % 10            
                #print ("lineCharacter : ",lineCharacter)
                if lineCharacter == 1 :
                        lfirstChoice = line.split()
                        #print ("lfirstChoice ------------------------- : ",lfirstChoice)
                        sfirstChoice = lfirstChoice[0]
                        numfirstChoice = int(sfirstChoice)
                        #print ("numfirstChoice ------------------------ : ",numfirstChoice)
                        l1stArrange = []
                        l1stRowChoice = []
                elif 2<= lineCharacter and lineCharacter <=5 :
                        if numfirstChoice == (lineCharacter-1) :
                            l1stRowChoice = makeRowInt(line) 
                elif lineCharacter == 6 :
                        l2ndChoice = line.split()
                        #print ("l2ndChoice ------------------------- : ",l2ndChoice)
                        s2ndChoice = l2ndChoice[0]
                        num2ndChoice = int(s2ndChoice)
                        #print ("num2ndChoice ------------------------ : ",num2ndChoice)
                        l2ndArrange = []
                        l2ndRowChoice = []
                elif 7<= lineCharacter or lineCharacter == 0 :
                        if lineCharacter >= 7 :
                            lineCharacter = lineCharacter - 6
                            #print ("----------3333------------",lineCharacter)
                        if lineCharacter == 0 :
                            lineCharacter = 4
                            #print ("---------888888-------------")
                        if num2ndChoice == lineCharacter :
                            l2ndRowChoice = makeRowInt(line)
                            #print ("-------------66666---------")
                else :
                        print ("else sljdlakjaljdal")
                if (count % 10) == 0 :
                    caseCount = caseCount + 1
                    if len(l2ndRowChoice) == len(l1stRowChoice) and len(l2ndRowChoice) > 0 and len(l1stRowChoice) > 0 :
                            #print ("l1stRowChoice : ",l1stRowChoice," l2ndRowChoice : ",l2ndRowChoice)
                            match = 0
                            for i in range (0,4) :
                                for e in range (0,4) :
                                    if l1stRowChoice[i] == l2ndRowChoice[e] :
                                        match = match + 1
                                        answer = l1stRowChoice[i]
                            #print (match," : match in function")
                            if match == 1 :
                                set = answer
                            elif match > 1 :
                                set = 'Bad magician!'
                            elif match < 1 or match == 0 :
                                set = 'Volunteer cheated!'
                            else :
                                print ("nothing ---===")
                            sPla = 'Case #'+str(caseCount)+": "+str(set)+'\n'
                            print ("sPla : ",sPla)
                            LastString = LastString + sPla  
                            #print (LastString)                            
                            # = compareAndMatch(l1stRowChoice,l2ndRowChoice)

    count = count + 1
    #print (count," : count")
    
fo = open("magin-Small-output.out", "w")
fo.write(LastString);
#close opend file
fo.close()
    
               
