'''
Google Code Jam 2009
Round 2
A.

@author: Samuel Spiza
'''

#fileName = "A-practice.in"
#fileName = "A-small-attempt1.in"
fileName = "A-large.in"
file = open(fileName, "r")


def findmin(case):
    c = 0
    i = 0
    while i < len(case):
        j = 0
        while 0 < sum(case[i + j][i+1:]):
            j = j + 1
        c = c + j
        case = swapjup(case, i, j)
        i = i + 1
    return c

def swapjup(case, i, j):
    new = []
    new.extend(case[:i])
    new.append(case[i+j])
    new.extend(case[i:i+j])
    new.extend(case[i+j+1:])
    return new
        
    
i = -1
j = 0
string = ""

cases = []
for line in file:
    if i == -1:
        T = int(line.strip())
        i = 1
    elif i == 0:
        j = j + 1
        cases.append([])
        N = int(line.strip())
        i = N + 1
    else:
        cases[-1].append([int(x) for x in list(line.strip())])
    i = i - 1

file.close()

z = 1
for case in cases:
    string = string + "Case #" + str(z) + ": " + str(findmin(case)) + "\n"
    z = z + 1



    
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
