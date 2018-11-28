base = "ROYGBV"


def getNeighbor(index, colours, first):
    # For short case
    if index == -1:
        maxLen = max(colours[0],colours[2],colours[4])
    else:
        maxLen = max(colours[index-2],colours[index-4])
    for i in range(len(colours)):
        if index != first and colours[first] > 0:
            return first
        if colours[i] == maxLen and i != index:
            return i
    print("No nieghbors at " + str(index))
    return -1

def solve(n, col):
    modCol = [c for c in col]
    if max(col[0],col[2],col[4]) > int(n/2):
        return "IMPOSSIBLE"
    built = ""
    last = -1
    first = -1
    for i in range(n):
        index = getNeighbor(last, modCol, first)
        modCol[index] -= 1
        built += base[index]
        last = index
        if first == -1:
            first = index
    return built


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n,r,o,y,g,b,v = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    ans = solve(n,(r,o,y,g,b,v))
    print("Case #{}: {}".format(i, ans))
    # check out .format's specification for more formatting options

