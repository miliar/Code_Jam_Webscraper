# -*- coding: utf-8 -*-
'''
Created on 13 avr. 2013

@author: Marc2
'''

import sys, os, getopt, re

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def Process(content):
    result=[]
    
    for lawn in content:
        lawnLarge=lawn[0]
        lawnLong=lawn[1]
        i=0
        PatternImpossible = False
        while i<len(lawnLarge) and not PatternImpossible:
            j=0
            while j<len(lawnLong) and not PatternImpossible:
                cell=int(lawnLarge[i][j])
                lawnLargeArray=list(lawnLarge[i])
                k=0
                LargeNotOK=False
                while k<len(lawnLargeArray) and not LargeNotOK:
                    if int(lawnLargeArray[k])>cell:
                        LargeNotOK = True
                    k+=1
                
                lawnLongArray=list(lawnLong[j])
                k=0
                LongNotOK=False
                while k<len(lawnLongArray) and not LongNotOK:
                    if int(lawnLongArray[k])>cell:
                        LongNotOK = True
                    k+=1
                j+=1
                
                if LargeNotOK and LongNotOK:
                    PatternImpossible=True
            i+=1
        if PatternImpossible:
            result.append('NO')
        else:
            result.append('YES')
 
    return result

def parseContent(content):
    result=[]
    nbTestCases = int(content[0])
    i=1
    j=0
    while i<len(content):
        while j<nbTestCases:
            testCaseLong = int(content[i].split(' ')[0])
            testCaseLarge = int(content[i].split(' ')[1])
            i+=1
            k=0
            Lawn=[]
            LawnLong=[]
            LawnLarge=[]
            while k<testCaseLong:
                LawnLong.append(str(content[i]).replace(' ',''))
                i+=1
                k+=1
            l=0
            while l<testCaseLarge:
                large=''
                for line in LawnLong:
                   large+=line[l]
                LawnLarge.append(large)
                l+=1
            Lawn.append(LawnLong)
            Lawn.append(LawnLarge)
            result.append(Lawn)
            j+=1
        i+=1
        
    return result

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
             raise Usage(msg)

        currentFolder = os.path.dirname(os.path.realpath(__file__))
        inputFile = '%(path)s/%(filename)s' % {'path': currentFolder, 'filename': args[0]}
        input = open(inputFile, "r")
        content = input.read()
        contentArray = content.splitlines()
        input.close()
        ParsedContent = parseContent(contentArray)
        outputArray = Process(ParsedContent)
        outputFile = currentFolder+'/'+'.'.join(args[0].split('.')[:-1])+'.out'
        output = open(outputFile, 'w')
        counter=1
        for line in outputArray:
            output.write('Case #'+str(counter)+': '+line+'\n')
            counter+=1
        output.close()

    except Usage as err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())
    
