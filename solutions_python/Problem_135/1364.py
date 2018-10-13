import re
f = open('A-small-attempt1.txt')
ff = open('outputA-small-attempt.txt','w')

a = [set()] * 4
b = [set()] * 4

T = int(f.readline())
for ii in range(T):
    x = int(f.readline())
    for jj in range(4):
        line = f.readline()
        #print(line)
        a[jj] = set((line.strip()).split())
       # print(a[jj])
    y = int(f.readline())
    #print('#####')
    for jj in range(4):
        line = f.readline()
        #print(line)
        b[jj] = set((line.strip()).split())
       # print(b[jj])
    #print(b)
    c = a[x-1].intersection(b[y-1])
    if len(c)>1:
        ff.write('Case #'+str(ii+1)+': Bad magician!\n')
    elif len(c) == 0:
        ff.write('Case #'+str(ii+1)+': Volunteer cheated!\n')
    else:
        ff.write('Case #'+str(ii+1)+': '+c.pop()+'\n')
ff.close()
f.close()
