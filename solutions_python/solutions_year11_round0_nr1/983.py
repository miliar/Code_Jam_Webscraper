import sys

def move(buttons, cur, loco, nexto, locb, nextb, s):
    #how far can we move before b or o are at their location
    if buttons[cur][0] == "O":
        #move o
        m = abs(int(loco) - int(buttons[cur][1]))
        s = s + m
        loco = int(buttons[cur][1])
        if not nextb == -1:
            mb = int(locb) - int(nextb)
            if m >= abs(mb):
                locb = nextb
            else:
                if mb > 0:
                    locb = locb - m
                else:
                    locb = locb + m
    else:
        #move for b
        m = abs(int(locb) - int(buttons[cur][1]))
        s = s + m
        locb = int(buttons[cur][1])
        if not nexto == -1:
            mo = int(loco) - int(nexto)
            if m >= abs(mo):
                loco = nexto
            else:
                if mo > 0:
                    loco = loco - m
                else:
                    loco = loco + m
    return s, loco, locb

def getnext(buttons, cur, which):
    l = len(buttons)
    next = -1
    if l > 0:
        for i in range(cur, l):
            if buttons[i][0] == which:
                next = buttons[i][1]
                break
    return next

f = open('A-large.in', 'r')
i = 0
cur_case = 0
for line in f:

    if i == 0:
        t = line
        i = i + 1
        continue
    else:
        cur_case = cur_case + 1

    c = str.split(line)
    n = c[0]
    buttons = []

    for j in range(1,int(n)*2+1):
        if(j%2):
            r = c[j]
        else:
            p = int(c[j])
            buttons.append([r,p])
    cur = 0
    s = 0
    locb = 1
    loco = 1

    while(cur < len(buttons)):
        nextb = getnext(buttons, cur, "B")
        nexto = getnext(buttons, cur, "O")

        #print "loco:" + str(loco)
        #print "locb:" + str(locb)
        #print "nexto:" + str(nexto)
        #print "nextb:" + str(nextb)
        
        if nexto == -1 and nextb == -1:
            break;
        if buttons[cur][0] == "O":
            if loco == buttons[cur][1]:
                #o needs to push his button
                s = s + 1
                cur = cur + 1
                #print "    o push button"
                if not nextb == -1:
                    d = int(nextb) - locb
                    if(d > 0):
                        locb = locb + 1
                    elif(d < 0):
                        locb = locb - 1
            else:
                #print "     o move"
                s, loco, locb = move(buttons, cur, loco, nexto, locb, nextb, s)
        else:
            if locb == buttons[cur][1]:
                #push b button
                #print "     b push putton"
                s = s + 1
                cur = cur + 1
                
                if not nexto == -1:
                    d = int(nexto) - loco

                    if(d > 0):
                        loco = loco + 1
                    elif(d < 0):
                        loco = loco - 1
            else:
                #print "    b move"
                (s, loco, locb) = move(buttons, cur, loco, nexto, locb, nextb, s)
    print "Case #" + str(cur_case) + ": " + str(s)