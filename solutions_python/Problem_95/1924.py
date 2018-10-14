import sys
import os
import pprint

word_map = {
 ' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}

if __name__ == "__main__":
    in_f = open("A-small-attempt0.in", "r")
    out_f = open("A.output", "w")
    for lineno, line in enumerate(in_f):
        if lineno == 0:
            continue
        
        line = line.strip()
        outline = ""
        for c in line:
            outline += word_map[c]
        
        outline = "Case #%s: %s\n" % (lineno, outline)
        out_f.write(outline)
    in_f.close()
    out_f.close()
        
    
     

            
        
    