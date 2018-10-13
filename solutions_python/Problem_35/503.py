# Usage:
# python script.py input_file output_file
# If output_file is not specified, it simply
# writes the result to console
# Lines between #---v and #---^ are part of
# the template and should not be edited.

#----------v
import sys
#----------^

def flows(x, y):
    if res[y][x] != '?':
        return None
    posibles = []
    if x is not 0 and cases[n][y][x-1] < cases[n][y][x]:
        posibles.append((x-1, y))
    if x is not len(cases[n][0])-1 and cases[n][y][x+1] < cases[n][y][x]:
        posibles.append((x+1, y))
    if y is not 0 and cases[n][y-1][x] < cases[n][y][x]:
        posibles.append((x, y-1))
    if y is not len(cases[n])-1 and cases[n][y+1][x] < cases[n][y][x]:
        posibles.append((x, y+1))
    if len(posibles) is 1:
        return posibles[0]
    m = 999999
    mo = -1
    for p in range(len(posibles)-1, -1, -1):
        if cases[n][posibles[p][1]][posibles[p][0]] > m:
            posibles.pop(p);
            mo -= 1
        elif cases[n][posibles[p][1]][posibles[p][0]] < m:
            if mo is not -1:
                posibles.pop(mo)
            mo = p
            m = cases[n][posibles[p][1]][posibles[p][0]]
    if len(posibles) is 1:
        return posibles[0]
    order = [(x, y-1),(x-1, y),(x+1, y),(x, y+1)]
    for o in order:
        for p in posibles:
            if p == o:
                return p


def waterflow(x, y, ch):
    res[y][x] = ch
    if x is not 0 and flows(x-1, y) == (x, y):
        waterflow(x-1, y, ch)
    if x is not len(cases[n][0])-1 and flows(x+1, y) == (x, y):
        waterflow(x+1, y, ch)
    if y is not 0 and flows(x, y-1) == (x, y):
        waterflow(x, y-1, ch)
    if y is not len(cases[n])-1 and flows(x, y+1) == (x, y):
        waterflow(x, y+1, ch)

#----------v
output = None
if len(sys.argv) == 3:
    output = open(sys.argv[2], 'w')
input = open(sys.argv[1])
#----------^

cases = []
n = int(input.readline().split("\n")[0])
for a in range(n):
    i = input.readline().split("\n")[0].split(" ")
    case = []
    for x in range(int(i[0])):
        case.append(input.readline().split("\n")[0].split(" "))
    for y in range(len(case)):
        for x in range(len(case[0])):
            case[y][x] = int(case[y][x])
    cases.append(case);

#----------v
for n in range(len(cases)):
#----------^

    res = []
    letter = 'A'
    for y in range(len(cases[n])):
        res.append([])
        for x in range(len(cases[n][0])):
            if ((x is 0 or cases[n][y][x-1] >= cases[n][y][x]) and
            (x is len(cases[n][0])-1 or cases[n][y][x+1] >= cases[n][y][x]) and
            (y is 0 or cases[n][y-1][x] >= cases[n][y][x]) and
            (y is len(cases[n])-1 or cases[n][y+1][x] >= cases[n][y][x])):
                res[-1].append(letter)
                letter = chr(ord(letter)+1)
            else:
                res[-1].append('?')
    for y in range(len(cases[n])):
        for x in range(len(cases[n][0])):
            if res[y][x].isupper():
                waterflow(x, y, res[y][x])
    letter = 'a';
    for line in res:
        for ch in line:
            if ch.isupper():
                for y in range(len(res)):
                    for x in range(len(res[0])):
                        if res[y][x] is ch:
                            res[y][x] = letter
                letter = chr(ord(letter)+1)
    result = ""
    for line in res:
        result += "\n" + " ".join(line);

#----------v
    print("Case #"+str(n+1)+": "+result)
    if len(sys.argv) == 3:
        output.write("Case #"+str(n+1)+": "+result+"\n")
if len(sys.argv) == 3:
    output.close()
#----------^





