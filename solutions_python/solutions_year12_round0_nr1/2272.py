#!/usr/bin/env python
d = {
'a':('y'),
'b':('h'),    
'c':('e'),   
'd':('s'),     
'e':('o'),     
'f':('c'),     
'g':('v'),     
'h':('x'),     
'i':('d'),     
'j':('u'),     
'k':('i'),     
'l':('g'),     
'm':('l'),    
'n':('b'),     
'o':('k'),     
'p':('r'),     
'q':('z'),     
'r':('t'),     
's':('n'),     
't':('w'),     
'u':('j'),     
'v':('p'),     
'w':('f'),     
'x':('m'),    
'y':('a'),     
'z':('q'),     
' ':(' '),     
     } 

T = int(raw_input())
for i in xrange(T):
    final_str = ""
    G = raw_input()
    for j in G:
        final_str += d[j]
    print "Case #%d: %s" % (i+1, final_str)
    