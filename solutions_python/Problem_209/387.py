import math

T = input()

def getInt():
    return map(int, raw_input().split(' '))

for t in range(T):
    N, K = getInt()
    pancakes = []
    for n in range(N):
        r, h = getInt()
        s = r*2*h

        pancakes.append([r, s])
    pancakes.sort(reverse=True)
    
    ans = 0
    for n in range(N):
        pancake = pancakes[n]
        pancakes_temp = pancakes[:n] + pancakes[n+1:]
        pancakes_temp.sort(reverse=True, key=lambda x: x[1])
        pancakes_temp = pancakes_temp[:K-1]

        area = pancake[0]**2 + pancake[1] + sum([p[1] for p in pancakes_temp])
        if area>ans:
            ans = area
   
    print "Case #%d: %.6f"%(t+1, ans*math.pi)
