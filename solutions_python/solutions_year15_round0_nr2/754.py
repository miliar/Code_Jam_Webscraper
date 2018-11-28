def solve(piles):
    if (sum(piles) == 0):
        return 0
    if (max(piles) <= 2):
        return max(piles)
    # Do nothing
    newPiles = list(max(0,p-1) for p in piles)
    mx = 0
    for i in range(0, len(piles)):
        if (piles[i] > piles[mx]):
            mx = i
    if piles[mx] == 9:
        piles.append(6)
        piles[mx] = 3
    else:
        piles.append(piles[mx]/2)
        piles[mx] = piles[mx] - (piles[mx]/2)
#    print(str(newPiles) + " or " + str(piles))
    return min(solve(newPiles) + 1, solve(piles) + 1)

T = int(input())
for I in range(1, T+1):
    D = int(raw_input())
    p = list(int(k) for k in raw_input().split())
    print("Case #%d: %d" % (I, solve(p)))
