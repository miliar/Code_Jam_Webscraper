fin = open("B-small-attempt0.in","rt")
import math
t = fin.readline().rstrip('\n')
t = int(t)

fout = open("OUTPUT","wt")  
for ex in range(t):
    n = fin.readline().rstrip('\n').split(' ')
    p = int(n[1])
    n = int(n[0])
    ing = [float(x) for x in fin.readline().rstrip('\n').split(' ')]
    packs = []
    for pack in range(n):
        sizes = fin.readline().rstrip('\n').split(' ')
        sizes = [float(x) for x in sizes]
        sizes.sort()
        mypack = []
        for x in sizes:
            lower = math.ceil(x/(1.1*ing[pack]))
            upper = math.floor(x/(0.9*ing[pack]))
            if lower > upper: continue
            mypack.append((int(lower),int(upper)))
        packs.append(mypack)
    canmake = 0
    while len(packs[0]) > 0:
        fail = False
        badfail = False
        admit = packs[0].pop(0)
        for x in range(1,len(packs)):
            if len(packs[x]) == 0:
                badfail = True
                fail = True
                break
            curpack = packs[x].pop(0)
            while curpack[1] < admit[0]:
                if len(packs[x]) == 0:
                    badfail = True
                    fail = True
                    break
                curpack = packs[x].pop(0)
            if fail: break

            if curpack[0] > admit[1]:
                packs[x] = [curpack]+packs[x]
                fail = True
                break
            admit = (max(admit[0],curpack[0]),min(admit[0],curpack[0]))
            
        if badfail: break
        if not fail: canmake += 1
    s = "Case #"+str(ex+1)+": "+str(canmake)+"\n"
    fout.write(s)
    print s

  
fout.close()
