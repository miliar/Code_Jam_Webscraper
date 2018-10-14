import os
import sys
from string import maketrans

def main():
    mapFrom = "abcdefghijklmnopqrstuvwxyz"
    mapTo= "yhesocvxduiglbkrztnwjpfmaq"
    tempData = open("a-small-attempt2.in", "r")
    t = int(tempData.readline())
    out = ""
    trans = maketrans(mapFrom, mapTo)
    for i in range( t ):
        inp = tempData.readline()
        inp = inp.translate(trans)
        inp = "Case #" + str(i+1) + ": " + inp
        out += inp
    outData = open("out.o", "w")
    print(out)
    outData.write(out)

if __name__ == "__main__": main()
