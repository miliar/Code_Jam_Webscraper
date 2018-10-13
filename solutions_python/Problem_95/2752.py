import os
import sys
os.chdir("/Users/Keloysius/Desktop/")
firstFile = "A-small-attempt0.in.txt"
c = open(firstFile, 'r')
x = 0
dictThis = {"y":"a", "n":"b", "f":"c", "i":"d", "c":"e", "w":"f", "l":"g", "b":"h", "k":"i", "u":"j", "o":"k", "m":"l", "x":"m", "s":"n", "e":"o", "v":"p", "z":"q", "p":"r", "d":"s", "r":"t", "j":"u", "g":"v", "t":"w", "h":"x", "a":"y", "q":"z", " ":" ", "\n":"\n"}
for line in c:
    if x>0:
        print "Case #"+str(x)+": ",
        for char in line:
            print dictThis[char],;sys.stdout.softspace=False;
    x+=1
