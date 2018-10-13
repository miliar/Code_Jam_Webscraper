import sys
sys.stdin = open("A-large.in")
sys.stdout = open("A-large.out", "w")

t = int(input())
for _ in range(t):
    grid, k = input().split()
    grid = [x for x in grid]
    s = len(grid)
    k = int(k)
    flips = 0
    for i in range(s-k+1):
        if grid[i] == "-":
            flips += 1
            for j in range(k):
                if j < s:
                    grid[i+j] = "+" if (grid[i+j] == "-") else "-"
            
    if "-" in grid:
        ans = "Case #{}: IMPOSSIBLE".format(_+1)
    else:
        ans = "Case #{}: {}".format(_+1, flips)
    print(ans)

sys.stdout.close()
