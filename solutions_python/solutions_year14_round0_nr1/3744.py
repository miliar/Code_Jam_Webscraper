T = input()
#print T

for i in range(T):
    flag = 0
    f = input()
    fl = []
    for j in range(4):
        fl.append(raw_input().split())
        #print f,fl
    s = input()
    sl = []
    for j in range(4):
        sl.append(raw_input().split())
        #print s,sl

    ans = 0

    for x in fl[int(f)-1]:
        for y in sl[int(s)-1]:
            if x == y:
                if ans == 0:
                    ans = x
                else:
                    flag = 1
    if ans == 0:
        flag = 2

    if flag == 0:
        print "Case #"+str(i+1)+": "+str(ans)
    elif flag == 1:
        print "Case #"+str(i+1)+": Bad magician!"
    elif flag == 2:
        print "Case #"+str(i+1)+": Volunteer cheated!"
