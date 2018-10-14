import sys

def solveCase(n):
    pancakes, size = sys.stdin.readline().split(" ")
    size = int(size)
    
    flips = 0
    flipped = [False for i in range(len(pancakes))]

    for i in range(len(pancakes)):
        if (flipped[i]) == (pancakes[i] == "+"):
            flips += 1

            for j in range(size):
                if i + j >= len(pancakes):
                    print("Case #{}: IMPOSSIBLE".format(n))
                    return
                flipped[i + j] = not flipped[i + j]

    
    print("Case #{}: {}".format(n, flips))


t = int(sys.stdin.readline())

for i in range(t):
    solveCase(i + 1)
