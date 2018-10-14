#!/usr/bin/python
import sys

def optimal(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    score = 0

    for i in range(len(naomi)):
        target = ken[0]
        block = naomi[0]
        for j in naomi:
            if j > target:
                block = j
                break

        if block > target:
            score += 1
            naomi.remove(block)
            ken = ken[1:]
        else:
            naomi = naomi[1:]
            ken = ken[:-1]

    return score

def fair(naomi, ken):
    naomi = naomi[:]
    ken = ken[:]
    score = 0

    for i in range(len(naomi)):
        if naomi[-1] > ken[-1]:
            score += 1
            ken = ken[1:]
        else:
            ken = ken[:-1]
        naomi = naomi[:-1]

    return score

def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[1][:-2] + "out", "w")

    for case in range(1, int(infile.readline())+1):
        infile.readline()

        naomi = sorted(float(f) for f in infile.readline().split())
        ken  = sorted(float(f) for f in infile.readline().split())

        print("Case #{0}: {1} {2}".format(case, optimal(naomi, ken), fair(naomi, ken)), file=outfile)

if __name__ == "__main__":
        main()
