'''
Google Code Jam 2009
Round 1B
A.

@author: Samuel Spiza
'''

#fileName = "A-practice.in"
#fileName = "A-small-attempt0.in"
fileName = "A-large.in"
file = open(fileName, "r")

def toArray(string):
#    print " QQ "
#    print string
    string = string.strip()
    if " " not in string or string.index(")") < string.index(" "):
        temp = string.strip().split(")", 1)
        temp[0] = [temp[0]]
        return temp[0], temp[1]
    else:
        temp = string.split(" ", 1)
        temp[1], rest = toArray2(temp[1])
        return temp, rest
    
def toArray2(string):
#    print " PP " + string + " PP "
    temp = string.strip().split("(", 1)
    arr = [temp[0]]
    blah, rest = toArray(temp[1])
    arr.append(blah)
    blah, rest = toArray(rest.split("(", 1)[1])
    arr.append(blah)
    return arr, rest
    
def modTiere(arr):
    for i in range(len(arr)):
        temp = arr[i].strip().split()
        arr[i] = [temp[0], temp[2:]]
    return arr
  
i = -1
j = 0
string = ""

cases = []
for line in file:
    if i == -1:
        C = int(line.strip())
        i = 1
    elif i == 0:
        j = j + 1
        cases.append([])
        N = int(line.strip())
        i = N + 1
    else:
        cases[-1].append(line.strip())
    i = i - 1

file.close()

newcases = []
for c in range(C):
    newcases.append([cases[2*c + y] for y in range(2)])
for newcase in newcases:
    newcase[0] = "".join(newcase[0])

print newcases

for z in range(len(newcases)):
    print newcases[z][0]
    blahh = newcases[z][0].split("(", 1)[1]
    while " )" in blahh:
        blahh = blahh.replace(" )", ")")
    while ") " in blahh:
        blahh = blahh.replace(") ", ")")
    while " (" in blahh:
        blahh = blahh.replace(" (", "(")
    while "( " in blahh:
        blahh = blahh.replace("( ", "(")
    newcases[z][0] = toArray(blahh)[0]
    newcases[z][1] = modTiere(newcases[z][1])

print newcases


def recur(tier, bla):
    i = 1
    if 1 < len(bla):
        if bla[1][0] in tier[1]:
            i = recur(tier, bla[1][1])
        else:
            i = recur(tier, bla[1][2])
    return float(bla[0]) * i


for zz in range(len(newcases)):
    string = string + "Case #" + str(zz + 1) + ":\n"
    for tier in newcases[zz][1]:
#        string = sting + 
        temp = float(recur(tier, newcases[zz][0]))
#        temp = 1*10000000
        temp2 = str(temp%10000000)
        temp3 = list("0000000")
        for i in range(len(temp2)):
            temp3[6-i:6-i] = [temp2[len(temp2)-1-i]]
        temp3 = "".join(temp3)
        string = string + str(temp) + "\n"
    
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
