#! /usr/bin/env python2
#################################################################################
#     File Name           :     A.py
#     Created By          :     YIMMON, yimmon.zhuang@gmail.com
#     Creation Date       :     [2014-04-12 09:08]
#     Last Modified       :     [2014-04-12 09:19]
#     Description         :
#################################################################################

T = int(raw_input())
for cas in range(T):
    a = int(raw_input())
    aa = []
    for i in range(4):
        aa.append(map(int, raw_input().split()))
    b = int(raw_input())
    bb = []
    for i in range(4):
        bb.append(map(int, raw_input().split()))
    x = set(aa[a-1])&set(bb[b-1])
    s = "Case #%d: " % (cas+1)
    if len(x) == 0:
        print s + "Volunteer cheated!"
    elif len(x) > 1:
        print s + "Bad magician!"
    else:
        print s + "%d " % (list(x)[0])
