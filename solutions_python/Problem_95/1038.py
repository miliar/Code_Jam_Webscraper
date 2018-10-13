import sys
import os
import sys


lang = dict()
lang["y"] = "a"
lang["n"] = "b"
lang["f"] = "c"
lang["i"] = "d"
lang["c"] = "e"
lang["w"] = "f"
lang["l"] = "g"
lang["b"] = "h"
lang["k"] = "i"
lang["u"] = "j"
lang["o"] = "k"
lang["m"] = "l"
lang["x"] = "m"
lang["s"] = "n"
lang["e"] = "o"
lang["v"] = "p"
lang["z"] = "q"
lang["p"] = "r"
lang["d"] = "s"
lang["r"] = "t"
lang["j"] = "u"
lang["g"] = "v"
lang["t"] = "w"
lang["h"] = "x"
lang["a"] = "y"
lang["q"] = "z"
lang[" "] = " "

cases = sys.stdin.readline() 
loop = int(cases) + 1

for case in range(0, loop):
      text = sys.stdin.readline()      
      if (text != "\n"):
            translated = []
            for letter in text:
                  if (letter != '\n'):
                        translated.append(lang[letter])
            if(translated):
                  print "Case #"+str(case+1)+":", "".join(translated)      
                        
     
