#!/usr/bin/python
import os, sys

CHECK = False
table = [-1 for i in range(26)]

def addTranslation(source, dest):
    for (s, d) in zip(source, dest):
        if s != ' ':

            index = ord(s) - 97
            val = ord(d) - 97
            if CHECK:
                if table[index] != -1 and table[index] != val:
                    print "ERROR at index %d, oldVal %d, newVal %d" % ( index, table[index], val)
                    sys.exit(1)
            table[index] = val

def translateChar(s):
    if s == ' ':
        return ' '
    return chr(97 + table[ord(s) - 97])    

def translate(source):
    return ''.join([translateChar(s) for s in source])

def main(filename):
    addTranslation('yeq', 'aoz')
    addTranslation('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand')
    addTranslation('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
    addTranslation('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')
    #print table
    # stupid fixup
    used = [False for i in range(26)]
    sourceNotFound = -1
    for i in range(26):
        val = table[i]
        if val != -1:
            used[val] = True
        else:
            sourceNotFound = i
    for i in range(26):
        if not used[i]:
            table[sourceNotFound] = i
    #print table

    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        caseStr = fileLines[index][:-1]
        index += 1
        #print caseStr
        answer = translate(caseStr)
        print "Case #%d: %s" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
