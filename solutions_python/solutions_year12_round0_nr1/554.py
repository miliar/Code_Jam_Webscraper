#!/usr/bin/python

import sys

def isLetter(char):
    if ord(char.lower())>96 and ord(char.lower())<124:
       return True
    return False

def findMapping(samples):
    mapping = {'y':'a','e':'o','q':'z','z':'q'}
    
    #get mapping from given samples
    file = open(samples)
    googlerese=None
    for line in file:
        if googlerese is None:
           googlerese=line
        else:
           english=line
           for c in range(0,len(english)):
              e=english[c].lower()
              g=googlerese[c].lower()
              if isLetter(g) and not g in mapping:
                  mapping[g]=e
           googlerese=None

    print mapping	
	
    #for c in range(97,123):
    #   if (chr(c) in mapping):
    #       print chr(c)+"->"+ mapping[chr(c)]
    #   else:
    #      print "No mapping for "+chr(c)

def translate(line):
    mapping={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}
    out=""
    for c in line:
       if not isLetter(c):
          out+=" "
       else:
         out+=mapping[c.lower()]
    return out     

if __name__ == "__main__":
    #findMapping("samples")
    f = sys.stdin
    count = int(f.readline())
    for c in range(count): 
        line=f.readline()
        print "Case #%d: %s" %(c+1,translate(line))

