from collections import deque

def algo(O,B,seq):
    time, bpos, opos = 0, 1, 1
    oDone, bDone = False, False

    if len(O) > 0: o_goal = O.popleft()
    else: oDone = True

    if len(B) > 0: b_goal = B.popleft()
    else: bDone = True

    bd, od, cp = 0, 0, False

    s = 0
    
    while not (oDone and bDone):
        time += 1
        bd, od, cp = 0, 0, False

        if not bDone:

            if bpos > b_goal:
                bpos -= 1
                bd = 1

            if bpos < b_goal:
                bpos += 1
                bd = 1

            if bpos == b_goal  and not bd and seq[s] == "B" + str(bpos) and not cp:
                s += 1
                cp = True
                if len(B)  == 0:
                    bDone = True
                else: b_goal = B.popleft()

        if not oDone:
            if opos > o_goal:
                opos -= 1
                od = 1


            if opos < o_goal:
                opos += 1
                od = 1

            if opos == o_goal and not od and seq[s] == "O" + str(opos) and not cp:
                s += 1
                cp = True
                if len(O)  == 0:
                    oDone = True
                else: o_goal = O.popleft()



    return time

f = open("a.txt", "r")
content = f.readlines()

T =  int(content[0])

for j in xrange(1,T+1):
    content[j] = content[j].rstrip("\n")
    c = content[j].split(" ")

    N = int(c[0])
    i = 1
    O_actions, B_actions, seq = [], [], []
    
    while i < len(c):
        seq.append(c[i] + c[i+1])
        if c[i] == 'O':
            O_actions.append(int(c[i+1]))
            i += 2
            continue
        if c[i] == 'B':
            B_actions.append(int(c[i+1]))
            i += 2
            continue


    print "Case #{0}: {1}".format(j, algo(deque(O_actions), deque(B_actions),seq))
