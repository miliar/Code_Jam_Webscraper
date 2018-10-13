import sys
import logging
logging.basicConfig(level=logging.INFO)

def d(string):
    logging.debug(string)

def printAnswer(case_num, ans):
    print("Case #%d: %s" % (case_num + 1, ans))

def checkResult(grid, N, M):
    ans = "YES"
    grid_t = list(zip(*grid))
    flag = False
    for i in range(N):
        for j in range(M):
            if grid[i][j] != max(grid[i]) and grid[i][j] != max(grid_t[j]):
                ans = "NO"
                flag = True
                break
        if flag:
            break
    return ans


def main(filename):
    f = open(filename, 'r')
    testcases = int(f.readline().strip())
    for t in range(testcases):
        N, M = list(map(int, f.readline().strip().split(' ')))
        lawn = []
        for line in range(N):
            lawn.append(list(map(int, f.readline().strip().split(' '))))
        ans = checkResult(lawn, N, M)
        printAnswer(t, ans)

if __name__ == "__main__":
    main(sys.argv[1])
