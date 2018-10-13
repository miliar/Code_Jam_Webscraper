#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    
    #nacteni 2 cisel
    numbers = sys.stdin.readline()[:-1].split()
    n = int(numbers[0])
    pd = int(numbers[1])
    pg = int(numbers[2])

    ok_pd = False
    ok_pg = True

    if ((pd == 0) or (pd == 100)):
        ok_pd = True
    else:
        min_n = 100
        pd_pom = pd
        for i in range(2):
            if (pd_pom % 2) == 0:
                min_n = min_n / 2
                pd_pom = pd_pom / 2
            if (pd_pom % 5) == 0:
                min_n = min_n / 5
                pd_pom = pd_pom / 5
        if (min_n <= n):
            ok_pd = True
    if not ok_pd:
        print "Case #%d: Broken" %(actual_case)
    else:
        if (pg == 0):
            if (pd != 0):
                ok_pg = False
        if (pg == 100):
            if (pd != 100):
                ok_pg = False
        if ok_pg:
            print "Case #%d: Possible" %(actual_case)
        else:
            print "Case #%d: Broken" %(actual_case)
