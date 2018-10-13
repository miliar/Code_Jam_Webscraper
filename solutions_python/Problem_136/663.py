# Cookie Clicker
# https://code.google.com/codejam/contest/2974486/dashboard#s=p1
# Qual Round 2014 19 points

import sys

def main():
    infile = open(sys.argv[1], 'r')
    outfile = open(sys.argv[2], 'w')
    
    line = infile.readline()
    T = int(line)

    for t in range(1, T+1):
        line = infile.readline()
        C, F, X = line.strip('\n').split(" ")
        C = float(C)
        F = float(F)
        X = float(X)

        old_rate = 2.0
        maxtime = X/old_rate
        curtime = 0.0

        new_rate = old_rate + F
        newtime = C/old_rate + X/new_rate

        while newtime < maxtime:
            curtime += C/old_rate
            old_rate = new_rate
            maxtime = X/old_rate
            new_rate = old_rate + F
            newtime = C/old_rate + X/new_rate

        curtime += maxtime
        outfile.write("Case #%d: %.7f\n" % (t, curtime))
        print("Case #%d: %.7f\n" % (t, curtime))
        
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
