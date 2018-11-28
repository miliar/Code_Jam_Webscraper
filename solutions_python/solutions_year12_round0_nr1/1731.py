'''
Created on Mar 24, 2012

@author: fady
'''
f=open('A-small-attempt0.in','r')
outputfile=open('out','w')
numberOfEntries=int(f.readline())
arrayOfNormalArrangement=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arrayOfNewTongue=        ['y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q']
#==================
counter=0
while (counter<int(numberOfEntries)):
    counter=counter+1
    outputfile.write("Case #"+str(counter)+": ")
    line = f.readline()
    seperated=line.split()
    for word in seperated:
        for character in word:
            outputfile.write(arrayOfNewTongue[arrayOfNormalArrangement.index(character)])
        outputfile.write(' ')
    outputfile.write("\n")

