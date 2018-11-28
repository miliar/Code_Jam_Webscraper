from sys import stdout
mapping = [0]*26

code = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
code += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
code += "de kr kd eoya kw aej tysr re ujdr lkgc jv"
code += "y qee"

text = "our language is impossible to understand"
text += "there are twenty six factorial possibilities"
text += "so it is okay if you want to just give up"
text += "a zoo"

for i in range(len(code)):
    if not code[i] == ' ':
        mapping[ord(code[i])-97] = text[i]
for i in range(26):
    if (mapping[i] == 0): mapping[i] = 'q'

ns = input()
for n in range(int(ns)):
    c = input()
    print("Case #", n+1, ": ",sep="",end="") 
    for j in range(len(c)):
        if c[j] == ' ':
            print(c[j], end="")
        else:
            print(mapping[ord(c[j])-97],end="")
        stdout.flush()
    print("",end="\n")
