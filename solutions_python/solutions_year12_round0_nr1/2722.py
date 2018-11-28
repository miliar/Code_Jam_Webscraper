#Author: Alexander Peel

a = open("small-a.gen.in", "r") 
b = open("small-a.gen.out", "r") 
charMap = {'z': 'q', 'q': 'z'}
revCharMap = {'q': 'z'}
j=0
for x in range(3):
    line = a.readline()
    gLine = b.readline()
    for i in range(min(len(gLine),len(line))):
        if line[i] not in charMap.keys():
            charMap[line[i]] = gLine[i]
            revCharMap[gLine[i]] = line[i]

for x in sorted(revCharMap.keys()):
    print(x, revCharMap[x])

a.close()
b.close()

print("size:", len(charMap))
inp = open("A-small-attempt1.in", 'r')
out = open("small-a.out", 'w')

#for x in charMap.keys():
    #print(x, charMap[x])

T = int (inp.readline())
i = 1
for x in range(T):
    out.write("Case #" + str(i) + ": ")
    line = inp.readline()
    for c in line:
        out.write(charMap[c])
    i+=1

