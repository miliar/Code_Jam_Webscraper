from math import floor, ceil

def bathroomStalls(N, K):
    # Starting pos, width
    gaps = [[N,0]]
    maxWidth = N
    Ls = 0
    Rs = 0
    for i in range(0,K):
        maxWidth = 0
        # Find biggest gap
        for gap in gaps:
            maxWidth = max(maxWidth, gap[0])
        gap = [-1,N+1]
        for possibleGap in gaps:
            if possibleGap[0] == maxWidth and possibleGap[1] < gap[1]:
                gap = possibleGap
        # Split gap
        Ls = floor((gap[0] - 1) / 2)
        Rs = ceil((gap[0] - 1) / 2)
        if Ls != 0:
            gaps.append([Ls, gap[1]])
        if Rs != 0:
            gaps.append([Rs, gap[1] + Rs])
        gaps.remove(gap)
    return str(max(Ls, Rs)) + " " + str(min(Ls, Rs))

with open('C-small-1-attempt0.in', 'r') as f:
    caseCounter = 0
    for line in f:
        if caseCounter != 0:
            inputs = line.split(" ")
            N = int(inputs[0])
            K = int(inputs[1])
            print("Case #" + str(caseCounter) + ": " + bathroomStalls(N, K))
        caseCounter += 1
