t = int(input())
for case in range(t):
    line = input().split()
    d = int(line[0])
    n = int(line[1])
    slowest_horse_needs = 0
    for i in range(n):
        line = input().split()
        k = int(line[0])
        s = int(line[1])
        slowest_horse_needs = max(slowest_horse_needs, (d-k)/s)
    print("Case #" + str(case+1) + ":", d/slowest_horse_needs)