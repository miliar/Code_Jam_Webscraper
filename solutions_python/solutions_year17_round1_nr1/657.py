# python2
import sys
import os.path
from heapq import heapify, heappush, heappop
from collections import deque

def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    #--------------------------------INPUT---------------------------------
    T = int(input.readline())
    toout = 1
    lis11 = []
    while T:
        R,W = list(map(int, input.readline().split()))
        td = []
        for i in xrange(R):
            st = str(input.readline())
            lis = []
            for x in st:
                if x == '\n':
                    continue
                lis.append(x)
            td.append(lis)
        pos = dict()
        for i in range(R):
            for y in range(W):
                if td[i][y] == '?':
                    continue
                if td[i][y] in pos:
                    pos[td[i][y]].append([i,y])
                else:
                    pos[td[i][y]] = []
                    pos[td[i][y]].append([i,y])

        for x in pos:
            #print x
            for i in range(pos[x][0][0],pos[x][len(pos[x])-1][0]+1):
                for y in range(pos[x][0][1],pos[x][len(pos[x])-1][1]+1):
                        td[i][y] = x
        for i in range(R):
            for y in range(W):
                if td[i][y]=='?':
                    val = '?'
                    for j in range(y,W):
                        if td[i][j] != '?':
                            val = td[i][j]
                            break
                    if val == '?':
                        for j in range(0,W):
                            if td[i][j] != '?':
                                val = td[i][j]
                    td[i][y] = val
        for i in range(R):
            for y in range(W):
                if td[i][y]=='?':
                    val = '?'
                    for j in range(i,R):
                        if td[j][y] != '?':
                            val = td[j][y]
                            break
                    if val == '?':
                        for j in range(0,R):
                            if td[j][y] != '?':
                                val = td[j][y]
                    td[i][y] = val
        lis11.append("Case #"+str(toout)+":")
        for x in td:
            str1 = ''.join(x)
            lis11.append(str1)
        #print lis11
        toout+=1
        T-=1
    #print '\n'.join(map(str, td))
    output = '\n'.join(map(str, lis11))
    #-------------------------------OUTPUT----------------------------------
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


if __name__ == "__main__":
    main()
