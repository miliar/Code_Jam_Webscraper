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
    gridList=parseContent(content)
    for grid in gridList:
        #result.append('X')
        Xwon = False
        Owon = False
        GameNotTerminated = False
        counter = 0
        while not Xwon and not Owon and counter<len(grid):
            Xmatch = re.search(r'[XT]{4}',str(grid[counter]))
            Omatch = re.search(r'[OT]{4}',str(grid[counter]))
            Dotmatch = re.search(r'\.',str(grid[counter]))
            if Xmatch:
                Xwon = True
            elif Omatch:
                Owon = True
            if Dotmatch:
                GameNotTerminated = True
            counter+=1
        if not Xwon and not Owon:
            if GameNotTerminated:
                result.append('Game has not completed')
            else:
                result.append('Draw')
        elif Xwon:
            result.append('X won')
        else:
            result.append('O won')
        
    return result

def parseContent(content):
    result=[]
    i=0
    grid=[]
    C1, C2, C3, C4, D1, D2='', '', '', '', '', ''
    gridCounter=0
    while i<len(content):
        if i!=0 and content[i]!='':
            grid.append(content[i])
            C1+=content[i][0]
            C2+=content[i][1]
            C3+=content[i][2]
            C4+=content[i][3]
            D1+=content[i][gridCounter]
            D2+=content[i][3-gridCounter]
            gridCounter+=1
        if content[i]=='' or i==(len(content)-1):
            grid.append(C1)
            grid.append(C2)
            grid.append(C3)
            grid.append(C4)
            grid.append(D1)
            grid.append(D2)
            result.append(grid)
            grid=[]
            C1, C2, C3, C4, D1, D2='', '', '', '', '', ''
            gridCounter=0
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
    
