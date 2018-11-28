def getVals():
    f = open('G:\\codejam\\dictionary.txt', 'r+')
    string = f.read()
    dictionary = {}
    googler = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv','z','a','o']
    engler= ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up','q','y','e']
    for j in xrange(0,len(googler)):
        googlerese = googler[j]
        english = engler[j]

        gLetters = list(googlerese)
        eLetters = list(english)

        

        for i in xrange(0,len(gLetters)):
            print gLetters[i] + ' ' + eLetters[i]
            if not (dictionary.has_key(gLetters[i])):
                print gLetters[i]
                dictionary[gLetters[i]] = eLetters[i]

    for item  in dictionary.items():
        print str(item)
        f.write(str(item)+'\n')
    print len(dictionary)
    f.close()

def readDict(string):
    vals = string.split('\n')
    dictionary = {}
    for val in vals:
        print val[7]
        dictionary[val[2]] = val[7]
    return dictionary

if __name__ == '__main__':
    f = open('G:\\codejam\\dictionary.txt', 'r+')
    
    string = f.read()
    dictionary = readDict(string)

    
    inputFile = open('G:\\codejam\\A-small-attempt2.in', 'r+')
    outputFile = open('G:\\codejam\\output.out', 'r+')
    inputString = inputFile.read()
    splitString = inputString.split('\n')
    
    for j in xrange(1,len(splitString)):
        googlerese = splitString[j]
        gLetters = list(googlerese)
        output =''
        if len(splitString[j]) > 0:
            for i in xrange(0,len(gLetters)):
                output += dictionary[gLetters[i]]
            if not( j == len(splitString)-1):
                outputFile.write('Case #'+str(j)+': ' +output + '\n')
            else:
                outputFile.write('Case #'+str(j)+': ' +output)
    f.close()
    inputFile.close()
    outputFile.close()



def getVals():
    f = open('G:\\codejam\\dictionary.txt', 'r+')
    string = f.read()
    dictionary = {}
    googler = ['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv','z','a','o']
    engler= ['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up','q','y','e']
    for j in xrange(0,len(googler)):
        googlerese = googler[j]
        english = engler[j]

        gLetters = list(googlerese)
        eLetters = list(english)

        

        for i in xrange(0,len(gLetters)):
            print gLetters[i] + ' ' + eLetters[i]
            if not (dictionary.has_key(gLetters[i])):
                print gLetters[i]
                dictionary[gLetters[i]] = eLetters[i]

    for item  in dictionary.items():
        print str(item)
        f.write(str(item)+'\n')
    print len(dictionary)
    f.close()
