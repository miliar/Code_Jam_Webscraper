T = int(input())
for ind in range(T):
    dest, numHorses = map(int, input().split(" "))
    maxTime = 0
    for i in range(numHorses):
        spot, speed = map(int, input().split(" "))
        time = (dest-spot)/speed

        if time>maxTime:
            maxTime = time
    print("Case #%d: %.6f"%(ind+1,float(dest)/maxTime))
