#!/usr/bin/python

from math import ceil
from itertools import permutations


def dfs(package, n):
    if not n == 2:
        quit()
    kit = 0
    i1 = package[0]
    for i2 in list(permutations(package[1])):
        k = 0
        p = len(i1)
        # print i1, i2, p
        for i in range(0, p):
            if i1[i][2] >= i2[i][1] and i1[i][1] <= i2[i][2]:
                k += 1
        kit = max(kit, k)
    return kit

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0,t):
        s = raw_input()
        n, p = int(s.split()[0]), int(s.split()[1])
        recipe = raw_input()
        recipe = [int(x) for x in recipe.split()]
        package = []
        for j in range(0,n):
            s = [int(x) for x in raw_input().split()]
            l = []
            for k in range(0,p):
                l.append((s[k], int(ceil( float(s[k])/ float(recipe[j]) / 1.1)),  int(float(s[k])/float(recipe[j])/0.9)))
            package.append(l)
        
        # print "package = "
        # print package
        if n == 1:
            kit = 0
            for j in range(0,p):
                if package[0][j][2] >= package[0][j][1]:
                    kit += 1
        else:
            kit = dfs(package, n)
        print "Case #" + str(i + 1) + ":", kit
        
