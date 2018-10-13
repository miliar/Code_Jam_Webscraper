from util import *
import sys

def valid(n):
    S = str(n)
    for i in range(1,len(S)):
        if int(S[i-1]) > int(S[i]):
            return False
    return True

def verify(num, bound):
    for i in range(num+1,bound+1):
        if valid(i):
            return i
    return -1

def Q2(N):
    S = [int(i) for i in str(N)]

    for i in range(1,len(S))[::-1]:
        if S[i-1] > S[i]:
            S[i-1] -= 1
            for j in range(i,len(S)):
                S[j] = 9

    return int(''.join([str(i) for i in S]))


if __name__ == '__main__':
    T = -1
    counter = 1
    while True:
        try:
            if T == -1:
                T = input()
            N = input()
            print "Case #%d: %d" % (counter, Q2(N))
            counter += 1
        except EOFError:
            break
