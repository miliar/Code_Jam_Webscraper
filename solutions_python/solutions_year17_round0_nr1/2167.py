import sys

sys.stdin = open('flipper.in','r')
sys.stdout = open('flipper.out','w')

def flip(stuff,spat,start):
    for i in range(start,start+spat):
        if stuff[i] == '-':
            stuff[i] = '+'
        else:
            stuff[i] = '-'
T = int(input())

for i in range(T):
    S, K = input().split()
    temp = list(S)
    K = int(K)
    length = len(S)
    count = 0
    for j in range(length-K+1):
        if temp[j] == '-':
            flip(temp,K,j)
            count += 1
    if ''.join(temp) == '+'*length:
        print("Case #%d: %d" % (i+1, count))
    else:
        print("Case #%d: IMPOSSIBLE" % (i+1))

