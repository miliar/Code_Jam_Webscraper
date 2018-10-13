#Stanisław Kacprzak
import string

#I prepare dictionary from example
d=open('dictionary.txt','r')
dictionary=dict()
for line in d.readlines():
    dictionary[line[0]]=line[2]
d.close()

inputFile=open('A-small-attempt0.in','r')
outputFile=open('output.txt','w')
lineNumber=int(inputFile.readline())

for n in range(1,lineNumber+1):
    lineToTranslate=inputFile.readline()
    translation=""
    for c in lineToTranslate:
        if c in dictionary:
            translation+=dictionary[c]
        else:
            translation+=c
    outputFile.write("Case #" + str(n) + ": " + translation)
outputFile.close()
    
