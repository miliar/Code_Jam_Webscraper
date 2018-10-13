def CalculateLS(s, occupied):
    i = s-1
    while i>0 and occupied[i] == 0:
        i -= 1
    return s-i-1

def CalculateRS(s, occupied):
    i = s+1
    while i<len(occupied)-1 and occupied[i] == 0:
        i += 1
    return i-s-1


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    occupied = [0]*(n+2)
    occupied[0] = 1
    occupied[-1] = 1
    chosenMin = 0
    chosenMax = 0
    for p in range(k):
        rank = []
        for s in range(n+2):
            if occupied[s] == 0:
                LS = CalculateLS(s, occupied)
                RS = CalculateRS(s, occupied)
                rank.append((min(LS, RS), max(LS, RS), n+2-s))
        (chosenMin, chosenMax, idx) = sorted(rank)[-1]
        occupied[n+2-idx] = 1

    print("Case #{}: {} {}".format(i, chosenMax, chosenMin))