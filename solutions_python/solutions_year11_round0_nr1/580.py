import re, sys

sys.setrecursionlimit(1000000000)

def adjust(current,to):
    if int(current) == int(to):
        return int(current)
    elif int(current) > int(to):
        return int(current) - 1
    else:
        return int(current) + 1

def move(order,o,b,op,bp,s):
    #print order,o,b,op,bp,s
    if len(o) == 0:
        o = [1]
    if len(b) == 0:
        b = [1]
    if len(order) == 0:
        return s
    else:
        if order[0] is 'O':
            if op == int(o[0]):
                return move(order[1:],o[1:],b,op,adjust(bp,b[0]),s+1)
            else:
                return move(order,o,b,adjust(op,o[0]),adjust(bp,b[0]),s+1)
        else:
            if bp == int(b[0]):
                return move(order[1:],o,b[1:],adjust(op,o[0]),bp,s+1)
            else:
                return move(order,o,b,adjust(op,o[0]),adjust(bp,b[0]),s+1)
        


numCases = int(sys.stdin.readline())

cases = []

for n in range(numCases):
    cases.append(sys.stdin.readline().strip())

n = 1
for case in cases:
    case = re.split(r'\s+',case)
    buttons = int(case[0])
    case = case[1:]
    oSeq = []
    bSeq = []
    order = []
    for b in range(buttons):
        if case[0] == 'O':
            oSeq.append(case[1])
            order.append('O')
        else:
            bSeq.append(case[1])
            order.append('B')
        case = case[2:]
    print "Case #" + str(n) + ": " + str(move(order,oSeq,bSeq,1,1,0))
    n = n + 1
