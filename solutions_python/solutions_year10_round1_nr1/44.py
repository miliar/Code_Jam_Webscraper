def rotate(N, K, grid):
    grid = [[grid[j][i] for j in reversed(range(N))] for i in range(N)]
    for j in range(N):
        k = N - 1
        for i in reversed(range(N)):
            if grid[i][j] == ".":
                while k >= 0:
                    if grid[k][j] != ".":
                        grid[i][j] = grid[k][j]
                        grid[k][j] = "."
                        break
                    k -= 1
            k -= 1
    #print(*grid, sep="\n")
    return grid

def check(N, K, grid):
    winners = {"R": False, "B": False}
    for i in range(N):
        for j in range(N):
            c = grid[i][j]
            for di, dj in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if not (i + (K - 1) * di < N and 0 <= j + (K - 1) * dj < N):
                    continue
                win = True
                for k in range(K):
                    if grid[i + k * di][j + k * dj] != c:
                        win = False
                if win:
                    winners[c] = True
    return winners["R"], winners["B"]

def solve(N, K, grid):
    grid = rotate(N, K, grid)
    R, B = check(N, K, grid)
    return {(False, False): "Neither", (False, True): "Blue",
            (True, False): "Red", (True, True): "Both"}[R, B]
    
def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        grid = [list(input()) for j in range(N)]
        print("Case #{}:".format(i + 1), solve(N, K, grid))

if __name__ == "__main__":
    main()

