# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 08-04-2017

def intToArr(N):
    arr = []
    while(N>0):
        arr.append(N%10)
        N = N/10
    return list(reversed(arr))

def removeLeadingZero(N):
    leading = True
    index = 0
    while(leading):
        if N[index] == 0:
            index+=1
        else:
            leading = False
    return N[index:]

def tidyNumber(N):
    changement = -1
    for i in range(0, len(N)-1):
        if N[i]>N[i+1]:
            changement = i
            break
    while changement>=1 and N[changement]==N[changement-1]:
        changement -= 1
    if changement != -1:
        N[changement] -= 1
        for i in range(changement+1, len(N)):
            N[i] = 9

    N = removeLeadingZero(N)
    N = [str(i) for i in N]
    result = "".join(N)
    return result



T = int(raw_input())
for i in range(1, T + 1):
    N = int(raw_input())
    result = tidyNumber(intToArr(N))
    print("Case #{}: {}".format(i, result))
