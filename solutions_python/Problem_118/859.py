#benoni.boy
#Google Code Jam
#13 April 2013
import sys
from gmpy import *

sys.stdin = open('C:\GCJ\in.txt')
sys.stdout = open('C:\GCJ\out.txt', 'w')

def numOFS(s, e):
    n = str(sqrt(s))
    l = (len(n)//2) + 1
    palstart = int(n[:l])
    pal = int(str(palstart) + str(palstart)[:-1][::-1])
    while (pal**2) > s:
        palstart -= 1
        pal = int(str(palstart) + str(palstart)[:-1][::-1])
    while (pal**2) < s:
        palstart += 1
        pal = int(str(palstart) + str(palstart)[:-1][::-1])
    OFS = 0
    pal2 = pal**2
    while pal2 <= e:
        spal2 = str(pal2)
        if spal2 == spal2[::-1]: OFS += 1
        palstart += 1
        pal = int(str(palstart) + str(palstart)[:-1][::-1])
        pal2 = pal**2
    return OFS

def numEFS(s, e):
    n = str(sqrt(s))
    l = (len(n)//2) + (len(n) % 2)
    palstart = int(n[:l])
    pal = int(str(palstart) + str(palstart)[::-1])
    while (pal**2) > s:
        palstart -= 1
        pal = int(str(palstart) + str(palstart)[::-1])
    while (pal**2) < s:
        palstart += 1
        pal = int(str(palstart) + str(palstart)[::-1])
    EFS = 0
    pal2 = pal**2
    while pal2 <= e:
        spal2 = str(pal2)
        if spal2 == spal2[::-1]: EFS += 1
        palstart += 1
        pal = int(str(palstart) + str(palstart)[::-1])
        pal2 = pal**2
    return EFS

numFS = lambda s, e: numOFS(s, e) + numEFS(s, e)

T = eval(input())
for i in range(T):
    A, B = [int(num) for num in input().split()]
    print('Case #' + str(i + 1) + ':', numFS(A, B))

sys.stdin.close()
sys.stdout.close()
