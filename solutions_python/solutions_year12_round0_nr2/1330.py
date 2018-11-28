#!/bin/env python
import sys
import os
import argparse
import logging
import subprocess
_folder_path = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(_folder_path)

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('infilename')
    parser.add_argument('outfilename')
    args = parser.parse_args()

    inf = open(args.infilename, "r")
    outf = open(args.outfilename, "w")

    lines = inf.readlines()
    lines = lines[1:]
    for i, line in enumerate(lines):
        line = line.split()
        num_googlers = int(line[0])
        num_surprising = int(line[1])
        p = int(line[2])
        scores = map(int, line[3:])

        num_nonsup = 0
        num_sup = 0

        print "--- %s ---" % i
        min_score_nonsup = p + 2*max(p-1,0)
        min_score_sup = p + 2*max(p-2,0)
        print "min nonsup:", min_score_nonsup
        print "min sup:", min_score_sup
        print "num_surprising:", num_surprising
        print scores

        for score in scores:
            if score >= min_score_nonsup:
                num_nonsup += 1
                print score, "nonsup"
            elif score >= min_score_sup:
                num_sup += 1
                print score, "sup"
            else:
                print score, "non"

        total = num_nonsup + min(num_sup, num_surprising)
        writeline = "Case #%s: %s\n" % (i+1, total)
        print writeline,
        outf.write(writeline)









if __name__ == '__main__':
    main()
