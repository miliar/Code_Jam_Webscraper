from math import *

def computeArea(stack):
    ans = pi*(stack[0][0]**2)
    for i in stack:
        ans += 2*pi*i[1]*i[0]
    return ans


def solve(N,K,pancakes):
    pancakes.sort()
    pancakes.reverse()
    #print("pan = ",pancakes)
    ans=0
    for i in range(N):
        base = pancakes[i]
        #print("base = ",base)
        #print(pancakes[i+1:])
        left = [2*j[0]*j[1] for j in pancakes[i+1:]]
        left.sort()
        left.reverse()
        best = left[:K-1]
        #print("left = ",left,"best = ",best)
        ans = max([ans, sum(best)+(base[0]**2) + 2*base[0]*base[1]])
        #print("ans = ",ans, sum(best)+(base[0]**2)+2*base[0]*base[1])
    #print("\n\n")
    return ans*pi

f = open('A-large.in','r')
g = open('output.txt','w')

T = int(f.readline())
for ind in range(T):
	# read input
    [N,K] = [int(i) for i in f.readline().split()]
    pancakes = [[int(i) for i in f.readline().split()] for j in range(N)]

	# compute answer
    ans = solve(N,K,pancakes)

	# print to file
    g.write('Case #{}: {}\n'.format(ind+1,ans))

f.close()
g.close()

