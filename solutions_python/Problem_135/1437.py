#!/usr/bin/env python

def main():
    n = int(raw_input())
    for test_case in range(n):
        r1 = int(raw_input())
        row1 = []
        row2 = []
        for i in range(1,5):
            line = raw_input()
            if i == r1:
                row1 = map(int,line.split())
        r2 = int(raw_input())
        for i in range(1,5):
            line = raw_input()
            if i == r2:
                row2 = map(int,line.split())
        res = [e for e in row1 if e in row2]
        print "Case #%d:" % (test_case+1),
        if len(res) == 0:
            print "Volunteer cheated!"
        elif len(res) > 1:
            print "Bad magician!"
        else:
            print res[0]

if __name__ == '__main__':
    main()