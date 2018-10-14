#Tom Dobrow
#Google Code Jam  Round 1
#4-13-2013

def read_words(afile):
    words = []
    for line in afile:
            words.append(line.strip())
    return words

def CheckWin(L, checked):
    for i in range(4):       
        if ((L[4*i]==checked or L[4*i]=='T') and (L[4*i+1]==checked or L[4*i+1]=='T') and (L[4*i+2]==checked or L[4*i+2]=='T') and (L[4*i+3]==checked or L[4*i+3]=='T')):
            return True  
    for i in range(4):
        if ((L[i]==checked or L[i]=='T') and (L[i+4]==checked or L[i+4]=='T') and (L[i+8]==checked or L[i+8]=='T') and (L[i+12]==checked or L[i+12]=='T')):
            return True
    if ((L[0]==checked or L[0]=='T') and (L[5]==checked or L[5]=='T') and (L[10]==checked or L[10]=='T') and (L[15]==checked or L[15]=='T')):
        return True
    if ((L[3]==checked or L[3]=='T') and (L[6]==checked or L[6]=='T') and (L[9]==checked or L[9]=='T') and (L[12]==checked or L[12]=='T')):
        return True
    return False
    

def Run(someString):
    if CheckWin(someString, 'X'):                
        return 1
    if CheckWin(someString, 'O'):      
        return 2
    for i in range (16):
        if (someString[i]=='.'):
            return 4
    return 3


filename = open('Tim.txt' , 'r')
T = filename.readline()
aList = read_words(filename)
for i in range(int(T)):
    
    newString = ""
    newString += aList[5*i]
    newString += aList[5*i+1]
    newString += aList[5*i+2]
    newString += aList[5*i+3]
    
    outcome = Run(newString)
    if (outcome==1):
        output = 'X won'
    elif (outcome==2):
        output = 'O won'
    elif (outcome==3):
        output = 'Draw'
    else:
        output = 'Game has not completed'
    print 'Case #' + str(i+1) + ': ' + output

filename.close()