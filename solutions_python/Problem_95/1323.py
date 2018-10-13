#!/usr/bin/env python
import os

def getMappingsForListOfStrings(mappings, lstStr1, lstStr2):
    for i in range(0, len(lstStr1)):
        getMappingsForOneToOneString(lstStr1[i], lstStr2[i], mappings)
        
    return mappings

def getMappingsForOneToOneString(s1, s2, mappings):

    for i in range(0, len(s1)):
        if not s1[i] in mappings:
            mappings[s1[i]] = s2[i]
            #mappings[s2[i]] = s1[i]



def translateGooglereseToEnglish(googlerese, mappings):
    newStr = ""
    for c in googlerese:
        newStr += mappings[c]
        
    return newStr


def problemIO(inputFile, mappings):
    text = open(inputFile, "rb").read()
    lines = text.split("\n")
    
    #take first line - no. of test cases
    cases = int(lines[0].strip())
    
    #DS
    lstTranslatedStrings = []
    
    #handle each test case
    for line in lines[1:]:
        googlerese = line.strip()
        if(googlerese):
            lstTranslatedStrings.append(translateGooglereseToEnglish(googlerese, mappings))
        
        
    return lstTranslatedStrings


def formatOutput(outputFile, lstStrings):
    F = open(outputFile, "wb")
    
    for i in range(0, len(lstStrings)):
        out = "Case #" + str(i + 1) + ": " + lstStrings[i]
        print out
        F.write(out + "\r\n")
    
    
    F.close()
    
#unit tests
if __name__ == '__main__':
    fileLoc = "C:\\Users\\manish_ramani\\Dropbox\\projects\\google_codejam\\"
    
    #add default mappings
    mappings = {}
    #mappings['a'] = 'y'
    #mappings['o'] = 'e'
    #mappings['z'] = 'q'
    
    mappings['y'] = 'a'
    mappings['e'] = 'o'
    mappings['q'] = 'z'
    
    #get mappings
    mappings = getMappingsForListOfStrings(mappings,
    ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"], ["our language is impossible to understand",
    "there are twenty six factorial possibilities", "so it is okay if you want to just give up"])
    
    
    #print mappings, len(mappings)
    ##complete the remaining mappings
    #set1 = set()
    #set2 = set()
    #for k in mappings:
    #    set1.add(k)
    #    set2.add(mappings[k])
    #    
    #for ele in set1:
    #    if not ele in set2:
    #        print "1:", ele
    #        
    #for ele in set2:
    #    if not ele in set1:
    #        print "2:", ele
    #        
    #
    #remaining mapping is z -> q
    mappings['z'] = 'q'
            
    
    #takes input file and translate based on mappings
    lstStrings = problemIO(fileLoc + "A-small-attempt1.in", mappings)
    
    #write output to file
    formatOutput(fileLoc + "output.out", lstStrings)
    
