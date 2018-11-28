#!/usr/bin/env python
import os
import sys
t = int(sys.stdin.readline())

for test in range(t):
    elem_list = []
    line = sys.stdin.readline().split()

    friends = []
    enemies = []
    n = int(line.pop(0))
    for i in range(n):
        friends.append(line.pop(0))
    n = int(line.pop(0))
    for i in range(n):
        enemies.append(line.pop(0))
    n = int(line.pop(0))
    invoke = line.pop(0)

    friend = {}
    for f in friends:
        friend[(f[0],f[1])] = f[2]
        friend[(f[1],f[0])] = f[2]
    enemy = {}
    for f in enemies:
        enemy[(f[0],f[1])] = True
        enemy[(f[1],f[0])] = True

    for i in range(len(invoke)):
        if len(elem_list) > 0:
            if friend.has_key((elem_list[-1],invoke[i])):
                elem_list[-1] = friend[(elem_list[-1],invoke[i])]
            else:
                for j,e in enumerate(elem_list):
                    if enemy.has_key((e,invoke[i])):
                        elem_list = []
                        break
                if len(elem_list)>0:
                    elem_list.append(invoke[i])
        else:
            elem_list.append(invoke[i])



    print "Case #%d: " % (test+1),
    sys.stdout.write("[")
    for i,e in enumerate(elem_list):
        if i != 0:
            sys.stdout.write(", ")
        sys.stdout.write(e)
    print "]"

