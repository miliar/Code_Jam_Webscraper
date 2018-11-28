'''
Created on 12 Apr 2014

@author: bluca
'''
import sys
from itertools import izip, imap

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    num_cases = int(lines[0])
    lines = lines[1:]
    for case, line in izip(range(1, num_cases+1), lines):
        C, F, X = imap(float, line.strip().split(" "))
        rate = 2
        t = 0
        while (1):
            if X / (rate + F) + C / rate > X / rate:
                t += X / rate
                break
            else:
                t += C / rate
                rate += F
        
        print "Case #%d: %s" % (case, t)

if __name__ == '__main__':
    main()
