# -*- coding: utf-8 -*-
'''
Created on 13 avr. 2013

@author: Marc2
'''

import sys, os, getopt, re

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def palindrome(number):
    numberList=list(number);
    NOK=False
    i=0
    test=len(numberList)/2
    while i<(len(numberList)/2) and not NOK:
        firstChar=numberList[i]
        secondChar=numberList[len(numberList)-(i+1)]
        if firstChar!=secondChar:
            NOK=True
        i+=1
    return not NOK

def Process(content):
    result=[]
    
    i=1
    while i<len(content):
        if i!=0:
            contentArray = content[i].split(' ')
            minReal=int(contentArray[0])
            min=int(minReal**0.5)
            max=int(contentArray[1])
            j=min
            nbFair=0
            #nbFair=''
            while j<=max**0.5:
                if j**2>=minReal and palindrome(str(j)) and palindrome (str(j**2)):
                    nbFair+=1
                    #nbFair+=str(j**2)+' '
                j+=1
            result.append(str(nbFair))
        i+=1
 
    return result

def parseContent(content):
    result=content
        
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
    
