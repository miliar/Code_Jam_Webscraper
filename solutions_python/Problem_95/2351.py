#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      saurabh
#
# Created:     14/04/2012
# Copyright:   (c) saurabh 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import re
def main():
    # getting  input
    fileName=raw_input ('input file name')
    IP=open(fileName)
    inputLines=IP.readlines()
    num=int(inputLines[0])
    #num = int(raw_input())
    #ij=0
    ij=1
    outputList=[]
    convDict={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' ','':'','\n':''}
    while(ij<(num+1)):
        #ipline= raw_input()
        ipline= inputLines[ij]
        lineList= []
        jk=0
        while jk<len(ipline):
            lineList.append( convDict[ipline[jk]])
            jk = jk +1
        toline=''.join(lineList)
        #key='Case #'+str(ij+1)+': '
        key='Case #'+str(ij)+': '
        outputList.append(toline)
        ij=ij +1
    #printing Output
    ij=0
    while ij< len(outputList):
        key='Case #'+str(ij+1)+': '
        print key+outputList[ij]
        ij=ij+1
if __name__ == '__main__':
    main()
