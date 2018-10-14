#!/usr/bin/env python3.2
'''
Created on 13/04/2012

@author: laarguelles
'''

import sys
def transcriptFile(inputFile):
    
    fileR = open(inputFile)
    fileW = open("googlerese.out","w")
    cases = fileR.readline()
    cases = cases[:len(cases) -1]
    cases = int(cases)
    for i in range(0,cases):
        line = fileR.readline()       
        line = line[:len(line) - 1]
        trans = transcripLine(line)
        trans = ("Case #{0}: "+trans).format(i+1)+"\n"
        fileW.write(trans)        
        
    
    

def transcripLine(line):
    
            
    transcript = "yhesocvxduiglbkrztnwjpfmaq"
    
    lineT = ""
    for char in line:
        if(char != " "):
            
            lineT += transcript[(ord(char) - 97)]  
        else:
            
                lineT += char
    return lineT

def main():
    inputFile = False
    try:
        inputFile = sys.argv[1]
    except IndexError:        
        exit
    
    if(inputFile):
        
        transcriptFile(inputFile)
    
    
if __name__ == '__main__':
    main()