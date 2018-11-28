#!/usr/bin/env python

n = int(raw_input())
for i in range(n):
    abox = []
    lin = int(raw_input())-1
    for j in range(4):
        ll = raw_input()
        ll = ll.rstrip()
        vv = ll.split()
        for v in vv:
            abox.append(int(v))
    fst = []
    fst.append(abox[(lin * 4)+0])
    fst.append(abox[(lin * 4)+1])
    fst.append(abox[(lin * 4)+2])
    fst.append(abox[(lin * 4)+3])
    bbox = []
    lin = int(raw_input())-1
    for j in range(4):
        ll = raw_input()
        ll = ll.rstrip()
        vv = ll.split()
        for v in vv:
            bbox.append(int(v))
    snd = []
    snd.append(bbox[(lin * 4)+0])
    snd.append(bbox[(lin * 4)+1])
    snd.append(bbox[(lin * 4)+2])
    snd.append(bbox[(lin * 4)+3])
    ans = -1
    flag = 0
    for x in fst:
        if x in snd:
            flag += 1
            ans = x
    if flag == 1:
        print 'Case #' + str(i+1) + ': ' + str(ans)
    if flag > 1:
        print 'Case #' + str(i+1) + ': Bad magician!'
    if flag == 0:
        print 'Case #' + str(i+1) + ': Volunteer cheated!'
