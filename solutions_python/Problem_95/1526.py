f = open("A-small.in", "rt")

cases = int(f.readline())
output = ""
translation = {'y':'a','e':'o','q':'z'}

code = "ejp mysljylc kd kxveddknmc re jsicpdrysi".split(" ")
decode = "our language is impossible to understand".split(" ")

for x in range(len(code)):
    coded = code[x]
    decoded = decode[x]

    for y in range(len(coded)):
        if not translation.has_key(coded[y]):
            translation[coded[y]] = decoded[y]

code = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd".split(" ")
decode = "there are twenty six factorial possibilities".split(" ")

for x in range(len(code)):
    coded = code[x]
    decoded = decode[x]

    for y in range(len(coded)):
        if not translation.has_key(coded[y]):
            translation[coded[y]] = decoded[y]


code = "de kr kd eoya kw aej tysr re ujdr lkgc jv".split(" ")
decode = "so it is okay if you want to just give up".split(" ")

for x in range(len(code)):
    coded = code[x]
    decoded = decode[x]

    for y in range(len(coded)):
        if not translation.has_key(coded[y]):
            translation[coded[y]] = decoded[y]

alpha = "abcdefghijklmnopqrstuvwxyz"

for y in range(len(alpha)):
	if not translation.has_key(alpha[y]):
		codedLetter = alpha[y]

for y in range(len(alpha)):
	vals = translation.values()
	if not alpha[y] in vals:
		translation[codedLetter] = alpha[y]



for x in range(cases):
    case = x+1
    coded = f.readline().strip("\n")
    decoded = ""
    
    for y in range(len(coded)):
        if coded[y] == " ":
            decoded += " "
        else:
            decoded += translation[coded[y]]
    
                
    output += str.format("Case #{0}: {1}\n",case,decoded)

f.close()
f = open("A-small.out", "wt")
f.write(output)
f.close()
