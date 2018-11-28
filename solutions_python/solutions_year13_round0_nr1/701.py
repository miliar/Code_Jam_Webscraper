#!/usr/bin/env python

winningcases = [
                [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
                [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
                [0, 5, 10, 15], [3, 6, 9, 12]
               ]

def extractrow(raw, match):
    rawsize = len(raw)
    res = []
    for c in range(rawsize):
        if(raw[c] == match or raw[c] == 'T'):
            res.append(c)
    return res

def extractset(raw, match):
    rawsize = len(raw)
    res = []
    for c in range(rawsize):
        row = extractrow(raw[c], match)
        for r in range(len(row)):
            res.append(row[r] + (c * rawsize))
    return res

def checkwinner(raw, match):
    mark = extractset(raw, match)
    #print mark
    for win in winningcases:
        if(set(mark) & set(win) == set(win)):
            return True
        
def checkdraw(raw):
    for row in raw:
        #print raw[row]
        for c in raw[row]:
            if(c == '.'):
                return False
    return True

f = open('/home/zinuzoid/Downloads/A-large.in', 'r')

cases =  int(f.readline())

raw = {}

for case in range(cases):
    data = {}
    data[0] = list(f.readline().rstrip())
    data[1] = list(f.readline().rstrip())
    data[2] = list(f.readline().rstrip())
    data[3] = list(f.readline().rstrip())
    
    raw[case] = data
    
    f.readline() # skip new line
f.close()

f = open('/home/zinuzoid/Desktop/a.out', 'w')
for case in range(cases):
    if(checkwinner(raw[case], 'X')):
        s = 'Case #' + str(case + 1) + ': X won'
        print s
        f.write(s + '\n')
    elif(checkwinner(raw[case], 'O')):
        s = 'Case #' + str(case + 1) + ': O won'
        print s
        f.write(s + '\n')
    elif(checkdraw(raw[case])):
        s = 'Case #' + str(case + 1) + ': Draw'
        print s
        f.write(s + '\n')
    else:
        s = 'Case #' + str(case + 1) + ': Game has not completed'
        print s
        f.write(s + '\n')
        
f.close()



