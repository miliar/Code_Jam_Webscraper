
def proc(data):
    #    for i in range(0, 4):
    #    print data[4*i:4*i+4]

    for u in ['X', 'O']:

        for i in range(0, 4):
            res = True
            for j in range(0, 4):
                k = data[i*4+j]
                if (k == u or k == 'T') == False:
                    #   print k, 'NG'
                    res = False
                    break
                
            if res == True:
                return u + " won"


        for j in range(0, 4):
            res = True
            for i in range(0, 4):
                k = data[i*4+j]
                if (k == u or k == 'T') == False:
                    #print k, 'NG'
                    res = False
                    break
            
            if res == True:
                return u + " won"


        res = True
        for i in range(0, 4):
            k = data[i*4+i]
            if (k == u or k == 'T') == False:
                #print k, 'NG'
                res = False
                break
        if res == True:
            return u + " won"

        res = True
        for i in range(0, 4):
            k = data[i*4+3-i]
            if (k == u or k == 'T') == False:
                #print k, 'NG'
                res = False
                break
        if res == True:
            return u + " won"
    
    for i in range(0, 16):
        if data[i] == '.':
            return "Game has not completed"

    return "Draw"

CaseNum = 0
i = 0
num = 4
index = 1
data = []
skip = True
for line in open('A-large.in', 'r'):
    #for line in open('input.txt', 'r'):
    if skip == True:
        #        CaseNum = int(line)
        skip = False
        i += 1
        continue

    line2 = line.split('\n')[0]
    data += line2
    num -= 1
    if num  > 0:
        continue

    result = proc(data)
    print "Case #" + str(index) + ": " + result
    index += 1
    num = 4
    i += 1
    data = []
    skip = True

