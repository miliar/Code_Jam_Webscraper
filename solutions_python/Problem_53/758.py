#!/usr/bin/python
# -*-Python-*-
import sys
import string

def WriteAnswer(testNo, ans):
    print "Case #%d: %s" % (testNo, ans)

def TestCase(testNo):
    line =  sys.stdin.readline().split(" ")
    N = int(line[0])
    K = int(line[1])
    #print line
    #print (N, K)
    on = (K & (2**N - 1)) == (2**N - 1)
    if on: ans="ON"
    else: ans="OFF"
    WriteAnswer(testNo, ans)

# main
T = int(input())
for testNo in range(1, T+1):
   TestCase(testNo)
