#!/usr/bin/env python


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    Ac, Aj = map(int, inFile.readline().split(' '))
    distributeTime = ['']*(24*60)
    Ct = 0
    Jt = 0
    for i in range(Ac):
        c, d = map(int, inFile.readline().split(' '))
        j = c
        Jt += d-c
        while j < d:
            distributeTime[j] = 'J'
            j += 1
    for i in range(Aj):
        j, k = map(int, inFile.readline().split(' '))
        c = j
        Ct += k-j
        while c < k:
            distributeTime[c] = 'C'
            c += 1
    # print distributeTime
    prev = ''
    # print Ct, Jt
    for i in range(24*60):
        if(distributeTime[i] == ''):
            distributeTime[i] = prev
            if(prev == 'c'):
                Ct += 1
            elif(prev == 'j'):
                Jt += 1
        elif(distributeTime[i] == 'C'):
            prev = 'c'
        elif(distributeTime[i] == 'J'):
            prev = 'j'
    # print distributeTime
    i = 0
    while(distributeTime[i] == ''):
        distributeTime[i] = prev
        i += 1
        if(prev == 'c'):
            Ct += 1
        elif(prev == 'j'):
            Jt += 1
    subs = ''
    pattern = []
    if(Ct < Jt):
        diff = (24*30) - Ct
        subs = 'c'
        pattern = [('j', 'C'), ('j', 'c')]
    else:
        diff = (24*30) - Jt
        subs = 'j'
        pattern = [('c', 'j'), ('c', 'J')]
    # print subs
    # print pattern
    # print distributeTime
    for z in range(2):
        prev = distributeTime[0]
        i = (24*60) - 1
        while(diff != 0 and i >= 0):
            present = distributeTime[i]
            if((present, prev) in pattern):
                diff -= 1
                distributeTime[i] = subs
            prev = distributeTime[i]
            i -= 1
    # if(diff != 0):
    #     i
    ans = 0
    prev = distributeTime[-1].upper()
    for present in distributeTime:
        pres = present.upper()
        if(prev != pres):
            ans += 1
        prev = pres
    # print diff
    # print distributeTime
    # print ans
    if(diff != 0):
        lrList = [0]
        if(subs == 'c'):
            lr = 'j'
        if(subs == 'j'):
            lr = 'c'
        prev = ''
        # if(distributeTime[0] == lr):
        #     lrList.append(0)
        for pres in distributeTime:
            # print lrList
            if(pres == lr):
                lrList[-1] += 1
            elif(lrList[-1] != 0):
                lrList.append(0)
        # print lr
        # print lrList
        if(distributeTime[-1] == lr and distributeTime[0] == lr):
            x = lrList.pop(0)
            lrList[-1] += x
        lrList.sort()
        lrList.reverse()
        # print lrList
        # print ans
        while(diff > 0):
            x = lrList.pop(0)
            diff -= x
            ans += 2
    outFile.write("Case #{}: {}\n".format(test, ans))
