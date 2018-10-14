import sys
import os
import math

sys.setrecursionlimit(200000)

def main():
    s = ''.join(sys.stdin.readlines()).split()
    os.close(0)

    N = int(s[0])
    s = s[1:]

    for i in range(N):
        P = int(s[0])
        Q = int(s[1])
        s = s[2:]
        toRelease = []
        for j in range(Q):
            toRelease += [int(s[0])]
            s = s[1:]


        count = 0
        perms = makePerms(toRelease)
        bestCount = P * P
        for k in perms:
            count = 0
            cells = [1] * P
            while len(k) > 0:
                #j = middlest(P, toRelease,cells)
                j = k[0]
                k = k[1:]
                cells[j-1] = 0
                count += anger(cells,j)
            if count < bestCount: 
                bestCount = count

        print "Case #" + str(i+1) + ": " + str(bestCount)


def makePerms(list):
    if len(list)==0:
        return []
    if len(list)==1:
        return [list]
    else:
        toRet = []
        for i in range(len(list)):
            subPerms = makePerms(list[0:i] + list[i+1:])
            toRet += map(lambda X: [list[i]] + X, subPerms)
        return toRet

#def middlest(P, toRelease, cells):
    #zeroes = []
    #for i in range(len(cells)):
    #    if cells[i]==1:
    #        zeroes+=[i]

    #minDist = P+1
    #release = P+1
    #for i in toRelease:
        #lb = 1
        #ub = P
        #for j in range(len(zeroes)):
           # if zeroes[j] < i and (j==len(zeroes)-1 or i < zeroes[j+1]):
          #      lb = zeroes[j]
         #       ub = zeroes[j+1]
        
        #middle = (ub-lb+1)/2
        #if (ub-lb+1)%2 ==1:
        #    middle +=1 
       # if abs(i-middle) < minDist:
      #      minDist = abs(i-middle)
     #       release = i
    #return release

def anger(cells, release):
    total = 0
    leftCells = cells[0:release-1]
    leftCells = leftCells[findright(leftCells,0)+1:]
    rightCells = cells[release:]
    rightCells = rightCells[0:findleft(rightCells,0)]

    return count(leftCells,1) + count(rightCells,1)

def count(list, item):
    count = 0
    for i in list:
        if i==item:
            count +=1
    return count

def findleft(list, item):
    for i in range(len(list)):
        if list[i]==item:
            return i
    return len(list)

def findright(list, item):
    for i in range(len(list)-1,-1,-1):
        if list[i]==item:
            return i
    return -1

if __name__ == "__main__":
 	main()

