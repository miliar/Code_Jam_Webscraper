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
    i=1
    while i < len(content):
        ArminMote = int(content[i].split(' ')[0])
        NbMotes = int(content[i].split(' ')[1])
        OtherMotesTmp = content[i+1].split(' ')
        OtherMotes = []
        for mote in OtherMotesTmp:
            OtherMotes.append(int(mote))
        
        nbOpeCumul = 0
        nbOpe = 0
        j=0
        OtherMotes.sort()
        if ArminMote == 1:
            nbOpeCumul =+ len(OtherMotes)
        else:
            while j < len(OtherMotes):
                mote = OtherMotes[j]
                if ArminMote>int(mote):
                    ArminMote += int(mote)
                    if nbOpe > (len(OtherMotes)-j):
                        nbOpeCumul += (len(OtherMotes)-j)
                        break
                    else:
                        nbOpeCumul += nbOpe
                        nbOpe = 0
                    j += 1
                else:
                    ArminMote += ArminMote-1
                    nbOpe += 1
                #if j == (len(OtherMotes)-1):
                #    nbOpeCumul += nbOpe
        
        result.append(str(nbOpeCumul))
        print("result : "+str(nbOpeCumul))
        i += 2
        
    return result

def parseContent(content):
     pass

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
        outputArray = Process(contentArray)
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
    
