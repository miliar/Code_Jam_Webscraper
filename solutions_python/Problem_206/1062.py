t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    D, N = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    slowestHorseS = 0
    slowestHorseD = D
    slowestHorseT = 0.0
    for x in range(N):
        horseD,horseS = [int(s) for s in input().split(" ")]
        if (D-horseD)*1.0/horseS>slowestHorseT:
            slowestHorseS = horseS
            slowestHorseD = horseD
            slowestHorseT = (D-horseD)*1.0/horseS
    print("Case #{}: {}".format(i, D/slowestHorseT))
