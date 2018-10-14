import sys, os

infile = open('B-large.in', 'r')
output = open('surprise.out', 'w')

def doProblem(inStr):
    things = inStr.split()
    n = int(things[0])
    s = int(things[1])
    p = int(things[2])
    scores = []
    for i in range(0, n):
        scores.append(int(things[3+i]))
    scores.sort()

    winners = 0
    for score in scores:
        nosurp = False
        for i in range(p, 11):
            for j in range(i-1, i+2):
                for k in range(i-1, i+2):
                    if i+j+k == score:
                        if i >= 0 and i <= 10 and j >= 0 and j <= 10:
                            if k >= 0 and k <= 10:
                                nosurp = True
        if nosurp:
            winners += 1
        else:
            nosurp = False
            for i in range(p, 11):
                for j in range(i-2, i+3):
                    for k in range(i-2, i+3):
                        if i+j+k == score:
                            if i >= 0 and i <= 10 and j >= 0 and j <= 10:
                                if k >= 0 and k <= 10:
                                    nosurp = True
            if nosurp and s > 0:
                s -= 1
                winners += 1
                
#    print scores

    return str(winners)

def println(line):
    print line
    output.write(line + "\n")

lines = infile.readlines()
cases = int(lines[0])
for i in range(0, cases):
    println("Case #" + str(i+1) + ": " + doProblem(lines[i+1].strip()))
    
infile.close()
output.close()
