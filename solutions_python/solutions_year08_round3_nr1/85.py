#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    #nacteni 1 cisla
    
    #nacteni 2 cisel
    numbers = sys.stdin.readline()[:-1].split()
    p = int(numbers[0])
    k = int(numbers[1])
    l = int(numbers[2])

    line = sys.stdin.readline()[:-1].split()
    list = []
    #nacitani cisel v radku do promenne
    for i in range(l):
        list.append(int(line[i]))

    list.sort()
    list.reverse()

    count = 0
    if l > k*p:
        print "Case #%d: Impossible" %actual_case

    else:
        for i in range(l):
            count += list[i]*(1+i/k)
     
        print "Case #%d: %d" %(actual_case,count)
