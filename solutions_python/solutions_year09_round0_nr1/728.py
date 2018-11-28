#!/usr/local/bin/python
import sys
import string
import re

def main(argv=None):
    if len(sys.argv)!=2:
        print "Usage: %s <file>\n" % sys.argv[0]
        sys.exit(-1)
    infile=sys.argv[1]
    f=open(infile,"r")
    meta=f.readline()
    metalist=string.split(meta," ")
    wordlen=int(metalist[0])
    dictlen=int(metalist[1])
    cases=int(metalist[2])
    #print "WL: %d DL: %d C: %d" % (wordlen,dictlen,cases)
    words=[]
    for i in range(0,dictlen):
        words.append(string.strip(f.readline()))
        if len(words[i]) > wordlen:
            words[i]=words[i][0:wordlen+1]
    #print words
    for j in range (0,cases):
        matches=0
        case=string.strip(f.readline())
        case=string.replace(case,"(","[")
        case=string.replace(case,")","]")
        casere=re.compile(case)
        for w in words:
            if casere.match(w):
                matches=matches+1
        print "Case #%d: %d" %(j+1,matches)
        


if __name__ == "__main__":
    sys.exit(main())
        
