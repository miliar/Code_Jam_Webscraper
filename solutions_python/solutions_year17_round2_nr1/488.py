t = int(input())

for i in range(1, t + 1):
    d, n = [int(s) for s in input().split(" ")]
    horses = []

    for x in range(n):
        horses.append([int(s) for s in input().split(" ")])
    
    horses.sort()
    horses = horses[::-1]

    max_time = 0

    for horse in horses:
        max_time = max(max_time, float(d - horse[0])/horse[1])

     
    print ("Case #{0}: {1}".format(i, float(d)/max_time))
