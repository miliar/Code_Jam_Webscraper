#!/usr/bin/python

f = open("data.txt")

case = None 

mapping = {
    'a' : 'y',
    'b' : 'n',
    'c' : 'f',
    'd' : 'i',
    'e' : 'c',
    'f' : 'w',
    'g' : 'l',
    'h' : 'b',
    'i' : 'k',
    'j' : 'u',
    'k' : 'o',
    'l' : 'm',
    'm' : 'x',
    'n' : 's',
    'o' : 'e',
    'p' : 'v',
    'q' : 'z',
    'r' : 'p',
    's' : 'd',
    't' : 'r',
    'u' : 'j',
    'v' : 'g',
    'w' : 't',
    'x' : 'h',
    'y' : 'a',
    'z' : 'q'       
}

rev_mapping = dict((value,key) for key,value in mapping.iteritems())

def decode( s ):
    return "".join([rev_mapping[l] for l in s.strip()])

cases = None
case = 0 ;
for line in f:
    if cases is None:
           cases = int(line)
           continue
    #end if 
    case = case + 1 
    sentance=""
    for word in line.split(" "):
        sentance = sentance + decode(word) + " "
    #end if:
    print "Case #"+str(case)+": "+sentance.strip()

#end for 

