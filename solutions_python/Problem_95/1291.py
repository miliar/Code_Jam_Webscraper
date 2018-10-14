dictionary = {"y": "a", "e": "o", "q": "z", "z": "q", " ": " ", "\n": "\n"}

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
a += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
a += "de kr kd eoya kw aej tysr re ujdr lkgc jv"

b = "our language is impossible to understand"
b += "there are twenty six factorial possibilities"
b += "so it is okay if you want to just give up"

for i, c in enumerate(a):
    if c is not " ":
        dictionary[c] = b[i]

inp = open('A-small-attempt0.in', 'r+')
out = open('output.txt', 'r+')

n = int(inp.readline()) # number of lines

for i in range(n):
    
    out.write("Case #" + str(i+1) + ": ")
    line = inp.readline()
    for c in line:
        out.write(dictionary[c])