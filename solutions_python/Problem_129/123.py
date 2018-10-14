#!/usr/bin/python

import sys, datetime

def solve(n, m, trips):
    entering = {i:0 for i in range(n)}
    leaving = {i:0 for i in range(n)}
    cost = 0
    for (a,b,x) in trips:
        entering[a-1] += x
        leaving[b-1] += x
        k = b-a
        cost += x*(k*(n+1) - k*(k+1)/2)
    cards = {i:0 for i in range(n)}
    cards = [0]*(n+1)
    cost2 = 0
    for i in range(n):
        cards.pop(0)
        cards.append(entering[i])
        lv = leaving[i]
        j = n
        while lv > 0:
            if cards[j] > 0:
                if lv >= cards[j]:
                    lv -= cards[j]
                    if j < n:
                        k = n-j
                        pay = cards[j] * (k*(n+1)-k*(k+1)/2)
                        cost2 += pay
                    cards[j] = 0
                else:
                    if j < n:
                        k = n-j
                        pay = lv * (k*(n+1)-k*(k+1)/2)
                        cost2 += pay
                    cards[j] -= lv
                    lv = 0
            j -= 1

    return ((cost-cost2) % 1000002013)


def main():
    if len(sys.argv) < 2:
        print 'Please provide input file'
        print 'Usage: %s inputfile [outputfile]' % sys.argv[0]
        return
    timestart = datetime.datetime.now()
    inputFile = open(sys.argv[1])
    outputFile = open(sys.argv[2], 'w') if len(sys.argv) >= 3 else None
    testCases = int(inputFile.readline().strip())
    print '-----------------'
    print 'Test cases: %d ' % testCases
    if len(sys.argv) < 3:
        print 'No output file'
    else:
        print 'Writing to',sys.argv[2]
    print '-----------------'
    for testCaseNumber in range(1, testCases+1):

        n, m = map(int, inputFile.readline().strip().split())
        trips = []
        for i in range(m):
            trips.append(map(int, inputFile.readline().strip().split()))

        string = 'Case #%d: %d' % (testCaseNumber, solve(n, m, trips))

        print string
        if outputFile:
            outputFile.write(string + '\n')
    print '-----------------'
    if outputFile:
        outputFile.close()
        print 'Written to',sys.argv[2]
    else:
        print 'No output file'
    print 'Elapsed time: %s' % (datetime.datetime.now() - timestart)
    print '-----------------'

if __name__=='__main__':
    main()
