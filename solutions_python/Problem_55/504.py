# -*- coding: utf-8 -*-
import Queue

inp = open("C-small-attempt1.in","r")
outp = open("output.out","w")

lines = inp.readline()
lines = lines.split()
lines = int(lines[0])

for i in range (0,lines):
    outp.write ("Case #" + str(i+1) + ": ")
    test = inp.readline()
    test = test.split ()
    test[0] = int(test[0])
    test[1] = int(test[1])
    test[2] = int(test[2])
    groups = inp.readline ()
    groups = groups.split()
    money = 0
    next_group = 0
    qwaiting = Queue.Queue (test[2])
    for j in range (0,test[2]):
        groups[j] = int (groups[j])
        qwaiting.put(groups[j])

    qhavingfun = Queue.Queue (test[2])

    for k in range (0,test[0]):
        cap = 0
        while cap < test[1] and not qwaiting.empty():
            if next_group == 0:
                next_group = qwaiting.get()
                if cap + next_group > test[1]:
                    break
                else:
                    cap = cap + next_group
                    qhavingfun.put(next_group)
                    next_group = 0
            else:
                cap = cap + next_group
                qhavingfun.put(next_group)
                next_group = 0
        money = money + cap
        while not qhavingfun.empty():
            buf = qhavingfun.get()
            qwaiting.put (buf)

    outp.write (str(money) + "\n")
                

inp.close()
outp.close()
