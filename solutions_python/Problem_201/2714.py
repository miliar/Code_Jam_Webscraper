# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    occupied = [False for s in range(n+2)]
    occupied[0] = True
    occupied[n+1] = True
    overallMaxMin = -1
    overallMaxMax = -1
    for i in range(k):
        mins = [-1 for s in range(n+2)]
        maxs = [-1 for s in range(n+2)]
        overallMaxMin = -1
        overallMaxMax = -1
        selectedStallIndex = -1
        for stall in range(n+2):
            if not occupied[stall]:
                ls = 0
                rs = 0
                nextStall = stall + 1
                while not occupied[nextStall]:
                    rs += 1
                    nextStall += 1
                nextStall = stall - 1
                while not occupied[nextStall]:
                    ls += 1
                    nextStall -= 1
                if ls > rs:
                    mins[stall] = rs
                    maxs[stall] = ls
                else:
                    mins[stall] = ls
                    maxs[stall] = rs
                if overallMaxMin < mins[stall] or (overallMaxMin == mins[stall] and overallMaxMax <= maxs[stall]):
                    overallMaxMin = mins[stall]
                    overallMaxMax = maxs[stall]
                    selectedStallIndex = stall
        occupied[selectedStallIndex] = True
    print("Case #{}: {} {}".format(j, overallMaxMax, overallMaxMin))
    # check out .format's specification for more formatting options
