from sys import argv
from decimal import *

def open_file(filename):
    fin = open(filename)
    total_tests = int(fin.readline().strip())
    for i in range(total_tests):
        num_of_teams = int(fin.readline())
        a = []
        for j in range(num_of_teams):
            a.append(fin.readline().strip())
        process_output(a, i+1)
    fin.close()

#  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
def process_output(a, num):
    print "Case #%s:" %(num)
    wp = []
    for c in range(len(a)):
        b = list(a[c])
        b.pop(c)
        tt = 0
        won = 0
        for i in b:
            if i == '0'or i == '1':
                tt += 1
                if i == '1':
                    won += 1
        wp.append(Decimal(str(won))/Decimal(str(tt)))
    owp = []
    for c in range(len(a)):
        arr = []
        l = a[c]
        for i in range(len(l)):
            if l[i] == '1' or l[i] == '0':
                arr.append(i)
        abc = []
        for i in range(len(arr)):
            tt = 0
            won = 0
            opp = list(a[arr[i]])
            opp.pop(c)
            for k in opp:
                if k == '1' or k == '0':
                    tt += 1
                    if k == '1':
                        won += 1
            abc.append(Decimal(str(won))/Decimal(str(tt)))
        owp.append((sum(abc)/len(abc)))
    oowp = []
    for c in range(len(a)):
        tt, won = 0, 0
        arr = a[c]
        for j in range(len(arr)):
            if arr[j] == '1' or arr[j] == '0':
                tt += 1
                won += owp[j]
        oowp.append(Decimal(str(won))/Decimal(str(tt)))
    for i in range(0, len(oowp)):
        print Decimal(str(wp[i]))/Decimal('4') + Decimal(str(owp[i]))/Decimal('2')+ Decimal(str(oowp[i]))/Decimal('4')

                
open_file(argv[1])
getcontext().prec = 30
