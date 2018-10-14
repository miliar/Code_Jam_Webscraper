def solve(buttons):
    #print(buttons)
    pos = {"O": 1, "B": 1}
    last = {"O": 0, "B": 0}
    other = {"O": "B", "B": "O"}
    total = 0
    for r, p in buttons:
        d = max(abs(pos[r] - p) - last[r], 0)
        pos[r] = p
        total += d + 1
        last[other[r]] += d + 1
        last[r] = 0
    return total

def main():
    T = int(input())
    for i in range(1, 1 + T):
        line = input().split()
        N = int(line[0])
        buttons = [(line[2 * j + 1], int(line[2 * j + 2])) for j in range(N)]
        ans = solve(buttons)
        print("Case #%d: %s" % (i, ans))

if __name__ == "__main__":
    main()


