#!/usr/bin/python
import sys


def seq(line):
    l = line.split()
    combine = dict()
    opposed = dict()
    for x in list(l[1: 1+int(l[0])]):
        combine[x[0]+x[1]] = x[2]
        combine[x[1]+x[0]] = x[2]
    l = l[1+int(l[0]):]
    for x in list(l[1: 1+int(l[0])]):
        opposed[x] = 1
        opposed[x[1]+x[0]] = 1
    l = l[1+int(l[0]):]
    answer = ""
    for x in list(l[1]):
        if len(answer) == 0:
            answer = x
        else:
            key = answer[-1] + x
            if key in combine:
                answer = answer[:-1]
                answer += combine[key]
            else:
                clear =False
                for y in answer:
                    kkey = y + x
                    if kkey in opposed:
                        clear = True
                if clear:
                    answer = ""
                else:
                    answer += x
    a = '['
    for x in list(answer):
        a += x + ", "
    if a[-1] == " ":
        a = a[0:-2]
    a += "]"
    return a           


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    i = 0
    while i < T:
        i += 1
        line = sys.stdin.readline()
        print "Case #%s: %s" % (i, seq(line))

