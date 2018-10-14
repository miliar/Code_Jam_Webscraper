from itertools import combinations
import math

file = open("input")

counter_i = 1
counter_end_i = file.readline()

def calcu(c, panR, panH):
    result = 0
    R = 0
    for x in c:
        y=int(x)
	if panR[y] > R:
		R  = panR[y]
	result = result + panR[y]*panH[y]
    result = result * 2 * math.pi + math.pi * R * R
    return result

def solve(N, K, panR, panH, index):
    result = 0
    for c in combinations(index, K):
	tmp = calcu(c, panR, panH)
	if tmp>result:
		result = tmp
    return result


while (counter_i <= int(counter_end_i.strip())):
    panR=[]
    panH=[]
    index=[]
    num = file.readline().strip().split(' ')
    N = int(num[0])
    K = int(num[1])
    for x in range(0,N):
        index.append(int(x))
    	pancake = file.readline().strip().split(' ')
    	panR.append(int(pancake[0]))
    	panH.append(int(pancake[1]))
    re = solve(N, K, panR, panH, index)
    counter_i=counter_i+1
    print "%s%d%s%0.9f"%("Case #", counter_i-1, ": ",re)
