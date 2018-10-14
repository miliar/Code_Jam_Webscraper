#!/usr/bin/python

import sys;
import os.path; 

def readi():
    return int(sys.stdin.readline().strip());

def readia():
    return [int(x) for x in sys.stdin.readline().strip().split()];

def readfa():
    return [float(x) for x in sys.stdin.readline().strip().split()];

def reads():
    return sys.stdin.readline().strip();

def check(stats, i, avg):
    res = 0;
    for stat in stats:
        res += abs(stat[i][1] - avg);
    return res;

def main():
    nt = readi();
    for t in range(1, nt+1):
        n = readi();
        stats = [];
        res = 0;
        for i in xrange(n):
            s = reads();
            stat = [];
            mainStat = None;
            prevC = s[0]; 
            curNumC = 0;
            for c in s:
                if c != prevC:
                    stat.append((prevC, curNumC));
                    curNumC = 1;
                    prevC = c;
                else:
                    curNumC += 1;
            stat.append((prevC, curNumC));
            #print (stat);
            stats.append(stat);
            if not mainStat:
                mainStat = stat;

        for stat in stats:
            if len(mainStat) != len(stat):
                res = -1;
                break;
            for (s1, s2) in zip(stat, mainStat):
                if s1[0] != s2[0]:
                    res = -1;
                    break;
            if res < 0:
                break;

        if res >= 0:
            totals = [0] * len(mainStat);          
            for stat in stats:
                for i in xrange(len(stat)):
                    totals[i] += stat[i][1];
            #print totals;         

            
            for i in xrange(len(mainStat)):
                avg = totals[i] // n;
                #print avg;
                res += min(check(stats, i, avg), check(stats, i, avg + 1));



        print "Case #%d: %s" % (t, str(res) if res >= 0 else "Fegla Won");

    

main();
