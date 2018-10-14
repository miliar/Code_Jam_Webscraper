import sys
import string

#map for language

def translate(dict, text):
    ans = ''
    for i in text:
        if i in dict:
            ans += dict[i]
        else:
            ans += ' '
    return ans
            



dict = {'y':'a', 'e':'o', 'q':'z'}

originalTexts = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

translatedTexts = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']


zippedList = []
for i in range(len(originalTexts)):
    for pair in zip(translatedTexts[i], originalTexts[i]):
        zippedList.append(pair)

#print zippedList

for pair in zippedList:
    if pair[0] not in dict:
        dict[pair[0]] = pair[1]

#print dict
#print len(dict)




#add missing alphabet
missedKey = ''
missedVal = ''
dictKeys = dict.keys()
dictVals = dict.values()
allTheLetters = string.lowercase
for i in allTheLetters:
    if i not in dictKeys:
        #print i
        missedKey = i
    if i not in dictVals:
        #print i
        missedVal = i
dict[missedKey] = missedVal    
        
#print dict

#ip = sys.stdin
ip = open('/Users/mohit/Downloads/A-small-attempt0.in', 'r')
numCase = int(ip.readline())

inputLines = []
for i in range(numCase):
    inputLines.append( ip.readline().rstrip('\n'))

for i in range(numCase):
    print 'Case #' + str(i+1) + ': ',translate(dict, inputLines[i])
