import sys

t = int(input())
for i in range(1, t + 1):
    [D, N]= [int(s) for s in input().split(" ")]
    horses = []
    for n in range(N):
    	[k, s]= [int(s) for s in input().split(" ")]
    	horses.append({'pos': k, 's': s})

    slowest = 0
    for horse in horses:
    	time = (D - horse['pos'])/horse['s']
    	slowest = max(slowest, time)

    max_speed = round(D / slowest * 1000000) / 1000000

    print("Case #{}: {}".format(i, max_speed))
