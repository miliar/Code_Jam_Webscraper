def cook(a, b):
    pancakes = list(a)
    spatulaSize = int(b)
    numFlips = 0

    for i in range(0, int(len(pancakes)) - spatulaSize + 1):
        if(pancakes[i] == "-"):
            numFlips += 1
            for j in range(0, spatulaSize):
                pancakes[i + j] = flip(pancakes[i + j])
    if ("-" in pancakes):
        return "IMPOSSIBLE"
    else:
        return numFlips




def flip(p):
    if p == "-":
        p = "+"
    else:
        p = "-"
    return p



def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        n, m = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
        print("Case #{}: {}".format(i, cook(n,m)))
        # check out .format's specification for more formatting options

main()