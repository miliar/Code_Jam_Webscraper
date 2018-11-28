inFile =open('B-small-attempt9.in', 'r')
outFile = open('out.txt', 'w')
lines = []

for i in inFile:
    lines.append(i.strip())

import random
def bad(listx):
    ct = 0
    while max(listx) != 0:
        listx.sort()
        i = random.randint(0, 1)
        if i == 0:
            listx = [i-1 for i in listx]
        else:
            t=random.randint(1, listx[-1])
            listx[-1] -= t
            listx = [t] + listx[:]
        ct += 1
    return ct

def sim(listx):
    minn = 9
    for i in range(10000):
        minn = min(minn, bad(listx[:]))

    return minn
i = 0
a=int(lines[0])
lines=lines[1:]
for i in range(a-1):
    luv=lines[2*i+1]
    outFile.write('Case #'+str(i+1)+': '+str(sim(list(map(int, luv.split(' '))))))
    outFile.write('\n')
i+=1
luv=lines[2*i+1]
outFile.write('Case #'+str(i+1)+': '+str(sim(list(map(int, luv.split(' '))))))
inFile.close()
outFile.close()
