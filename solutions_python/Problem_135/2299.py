#!/usr/bin/python
import sys

def main():
    CaseNum = int(sys.stdin.readline())
    FirstLineNum = 0
    FirstLineCards = []
    SecondLineNum = 0
    SecondLineCards = []
    for i in range(CaseNum):
        # read answer
        FirstLineNum = int(sys.stdin.readline())
        for j in range(4):
            cardlinestr = sys.stdin.readline()
            if j == FirstLineNum - 1:
                FirstLineCards = cardlinestr.split()
        SecondLineNum = int(sys.stdin.readline())
        for k in range(4):
            cardlinestr = sys.stdin.readline()
            if k == SecondLineNum - 1:
                SecondLineCards = cardlinestr.split()
        result = [x for x in FirstLineCards if x in SecondLineCards]
        print "case #" + str(i + 1) + ":",
        if len(result) == 1:
            print result[0]
        elif len(result) > 1:
            print "Bad magician!"
        else:
            print "Volunteer cheated!"

if __name__ == '__main__':
    main()
