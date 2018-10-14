#!/usr/bin/env python

f = open('C-small-attempt0.in','r')
lines2 = []
lines = f.xreadlines()
for line in lines:
    line = line.splitlines()[0]
    lines2.append(line)
del lines
f.close()
lines = lines2[1:]
del lines2

results = []
codejam = 'welcome to code jam'
for line in lines:
    counts = []
    value = 0
    for ch in codejam:
        pos = -1
        count = []
        while True:
            pos = line.find(ch,pos+1)
            if pos == -1:
                break
            count.append(pos)
        counts.append(count)
        
    for i in range(19):
        nLen = len(counts[i])
        if nLen == 0:
            value = 0
            break
    for n0 in counts[0]:
        for n1 in counts[1]:
            if n0>=n1:
                continue
            for n2 in counts[2]:
                if n1>=n2:
                    continue
                for n3 in counts[3]:
                    if n2>=n3:
                        continue
                    for n4 in counts[4]:
                        if n3>=n4:
                            continue
                        for n5 in counts[5]:
                            if n4>=n5:
                                continue
                            for n6 in counts[6]:
                                if n5>=n6:
                                    continue
                                for n7 in counts[7]:
                                    if n6>=n7:
                                        continue
                                    for n8 in counts[8]:
                                        if n7>=n8:
                                            continue
                                        for n9 in counts[9]:
                                            if n8>=n9:
                                                continue
                                            for n10 in counts[10]:
                                                if n9>=n10:
                                                    continue
                                                for n11 in counts[11]:
                                                    if n10>=n11:
                                                        continue
                                                    for n12 in counts[12]:
                                                        if n11>=n12:
                                                            continue
                                                        for n13 in counts[13]:
                                                            if n12>=n13:
                                                                continue
                                                            for n14 in counts[14]:
                                                                if n13>=n14:
                                                                    continue
                                                                for n15 in counts[15]:
                                                                    if n14>=n15:
                                                                        continue
                                                                    for n16 in counts[16]:
                                                                        if n15>=n16:
                                                                            continue
                                                                        for n17 in counts[17]:
                                                                            if n16>=n17:
                                                                                continue
                                                                            for n18 in counts[18]:
                                                                                if n17>=n18:
                                                                                    continue
                                                                                #if n0<n1 and n1<n2 and n2<n3 and n3<n4 and n4<n5 and n5<n6 and n6<n7 and n7<n8 and n8<n9 and n9<n10 and n10<n11 and n11<n12 and n12<n13 and n13<n14 and n14<n15 and n15<n16 and n16<n17 and n17<n18:
                                                                                else:
                                                                                    value +=1
    results.append(value)
index = 1    
for item in results:
    item = item % 10000
    print "Case #%d: %04d" % (index,item)
    index += 1
            