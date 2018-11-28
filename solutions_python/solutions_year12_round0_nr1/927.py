f = open("a.in")
numCases = int(f.readline())
d = {
     "a":"y",
     "b":"h",
     "c":"e",
     "d":"s",
     "e":"o",
     "f":"c",
     "g":"v",
     "h":"x",
     "i":"d",
     "j":"u",
     "k":"i",
     "l":"g",
     "m":"l",
     "n":"b",
     "o":"k",
     "p":"r",
     "q":"z",
     "r":"t",
     "s":"n",
     "t":"w",
     "u":"j",
     "v":"p",
     "w":"f",
     "x":"m",
     "y":"a",
     "z":"q",
     " ":" ",
     "\n":"\n"
     }
for (i,line) in enumerate(f):
    newline = ""
    for c in line:
        newline+=d[c]
    print "Case #%d: %s" %(i+1,newline),

