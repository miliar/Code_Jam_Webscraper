#! /usr/bin/python 2.7

import time
import sys

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    T = int(lines[0])
    counter = 1
    for case in range(T):
        givencase = case + 1
        line = lines[givencase].split()
        cookies(givencase,float(line[0]),float(line[1]),float(line[2]))
    f.close()

def cookies(case,C,F,X):
    totalTime = 0.0
    production = 2
    finish = False

    while(finish == False):
        time2 = float(X / production)

        time = float(C / production)
        time1 = time + float(X / (production + F))

        if time1 < time2:
            totalTime += time
            production += F
        elif time2 < time1:
            totalTime += time2
            finish = True
        else:
            totalTime += time1
            finish = True
    print "Case #"+str(case)+":",totalTime
    sys.stdout.flush()
    del totalTime, production, time1, time2

if __name__ == '__main__':
    main()
