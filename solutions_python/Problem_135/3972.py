import sys

f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    cnt = 0
    val = 0
    a1 = []
    a2 = []
    guess1 = int(f.readline()) - 1
    for i in range(4):
        a1.append(map(int, f.readline().split()))
        
    guess2 = int(f.readline()) - 1
    for i in range(4):
        a2.append(map(int, f.readline().split()))
    
    for i in range(4):
        #print a1[guess1][i]
        if a1[guess1][i] in a2[guess2]:
            cnt = cnt + 1
            val = a1[guess1][i]
        if cnt >= 2:
            break;

    print "Case #%d: " % ((t + 1)),
    if 0 == cnt:
        print "Volunteer cheated!"
    elif 1 == cnt:
        print "%d" % val
    else:
        print "Bad magician!"

f.close()
