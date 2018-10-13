import os
import pprint


translationTable = {}

alphabets = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for alphabet in alphabets:
    translationTable[alphabet] = "N/A"
g = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
e = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
for a,b in zip(g,e):
    translationTable[a] = b

translationTable['q'] = 'z'
translationTable['z'] = 'q'

#pprint.pprint(translationTable)

inputFilename = os.path.splitext(os.path.basename(__file__))[0]+".in"
inputFile = open(inputFilename,"r")

outputFilename = os.path.splitext(os.path.basename(__file__))[0]+".out"
outputFile = open(outputFilename,"w")


sampleNum = int(inputFile.readline().strip())
lstSample = []

for i in range(sampleNum):
    lstSample.append(inputFile.readline().strip())
    
for n,sample in enumerate(lstSample):
    z = "".join(map(lambda x:translationTable[x], sample))
    outputFile.write("Case #%s: %s"%(n+1,z)+"\n")


