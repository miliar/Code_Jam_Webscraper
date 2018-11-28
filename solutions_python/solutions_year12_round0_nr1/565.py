a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq'
b = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz'

mapping = {}
for i in range(len(a)):
    mapping[a[i]] = ord(b[i]) - ord(a[i])

def translate(instr):
    theString = ""
    for j in range(len(instr)):
        theString += chr(ord(instr[j]) + mapping[instr[j]])
    return theString

#print(translate(a))

filename = "D:\\codejam\\A-small-attempt0 (1).in"
out = open(filename + ".out", "w")
f = open(filename)
number = int(f.readline())
lines = f.read().splitlines()
for i in range(number):
    a = ("Case #" + str(i+1) + ": " + translate(lines[i]))
    print(a)
    out.write(a + "\n")