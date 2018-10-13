#!/usr/bin/python3

def isTidy(N):
    tempDigit = N[0]
    for i in range(1,len(N)):
        if N[i] >=  tempDigit:
          tempDigit = N[i]
        else: return False
    return True

def zeroAfterOne(N):
    for i in range(len(N)-1):
        if int(N[i]) == 1 and int(N[i+1]) == 0: return True
    return False

T = int(input())

for i in range(T):
    N = int(input())
    j = N
    notFound = True
    while(notFound):
        if zeroAfterOne(str(j)):
            if int(str(j)[0]) == 0: newFirstDigit = "9"
            else: newFirstDigit = str(int(str(j)[0]) - 1)
            
            j = int(newFirstDigit + "9"*(len(str(j))-1))
        if isTidy(str(j)):
            lastSeen = j
            notFound = False
        j -= 1
    print("Case #{}: {}".format(i+1, lastSeen))
