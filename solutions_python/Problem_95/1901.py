## Google code jam round 1

## Thomas Raway

## googlerese translation
## input file name should be round1.txt

from string import *

googlerese = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
english = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

googlerese.split()
english.split()
alphabet.split()

translateList = [['y','a'],['e','o'],['q','z']]

for i in range(len(googlerese)):
    flag = 0
    for j in range(len(translateList)):
        if(googlerese[i] == translateList[j][0]):
            flag = 1
            break

    
    if(flag == 0):
        translateList.append([googlerese[i],english[i]])


#finding the missing goolerese letter
for i in range(len(alphabet)):
    flag = 0
    for j in range(len(translateList)):
        if(translateList[j][0] == alphabet[i]):
            flag = 1

    if(flag == 0):
        missingG = alphabet[i]
        break


#finding the missing english letter
for i in range(len(alphabet)):
    flag = 0
    for j in range(len(translateList)):
        if(translateList[j][1] == alphabet[i]):
            flag = 1

    if(flag == 0):
        missingE = alphabet[i]
        break

translateList.append([missingG, missingE])
        
text = open('A-small-attempt0.in','r')

output = open('outputRound1.txt','w')

line = text.readline()
line.split()

num = 0

for line in text.readlines():
    num += 1
    line.split()
    newLine = []
    for char in line:
        for trans in translateList:
            if(char == trans[0]):
                newLine.append(trans[1])
                break
            
    output.write('Case #%d: %s\n' % (num, join(newLine, '')))
    
text.close()
output.close()



