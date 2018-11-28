import math
import re
f = open('A-small-attempt0.in', 'r')
wf = open('outputA1.out', 'w')
t = f.readline()
for i in range(int(t)):
    r1 = f.readline()
    t1 = []
    for j in range(4):
        str1 = f.readline()
        s1 = re.findall(r"[\w']+", str1)
        t1.append(s1)
    r2 = f.readline()
    t2 = []
    for j in range(4):
        str1 = f.readline()
        s1 = re.findall(r"[\w']+", str1)
        t2.append(s1)
    print r1, r2
    print t1
    print t2
    count = 0
    ans = ''
    for j in range(4):
        c1 = t1[int(r1)-1][j]
        for k in range(4):
            c2 = t2[int(r2)-1][k]
            if c1 == c2:
                count+= 1
                if count == 1:
                    ans = c1
    if count == 0:
        ans = 'Volunteer cheated!'
    elif count >1:
        ans = 'Bad magician!'



    wf.write('Case #'+str(i+1)+': '+ans+'\n')



f.close()
wf.close()
