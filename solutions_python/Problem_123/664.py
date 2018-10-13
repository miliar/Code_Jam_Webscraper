from copy import *
t = input()
for i in xrange(t):
    am,n = map(int,raw_input().split())
    motes = map(int,raw_input().split())
    motes.sort()
    oper = []
    op = 0
    delop = 0
    if am == 1:
        op = len(motes)
    else:
        for j in xrange(len(motes)):
            #print oper
            if j != 0:
                oper.append(copy(oper[j-1]))
            else:
                oper.append([0,0])
                
            if motes[j] < am:
                am += motes[j]
            else:
                delop = 0
                adop = 0
                if motes[j] - am >= am-1:
                    delop = len(motes) - j
                #print am,motes[j]
                while am <= motes[j]:
                    am += (am-1)
                    adop += 1
                am += motes[j]
                if delop == 0:
                    oper[j][0] += adop
                elif adop > delop:
                    oper[j][1] += delop
                else:
                    oper[j][0] += adop
        #print oper
        op = oper[-1][0] + oper[-1][1]
    print "Case #" + str(i+1) + ": " + str(op)
