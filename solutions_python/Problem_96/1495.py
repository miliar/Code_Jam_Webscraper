T = int(input())
for i in range(1,T+1):
    line = [int(x) for x in input().split()]
    N = line[0]
    S = line[1]
    p = line[2]
    scores = line[3:]
    count = 0
    for score in scores:
        if score >= 3*p-2:
            count += 1
        elif p > 1 and score >= 3*p-4 and S>0:
            count += 1
            S -= 1
    print("Case #"+str(i)+": "+str(count))
