from functools import lru_cache

@lru_cache(maxsize = None)  # Memoization.
def solve1(C, W):
    if C == W:
        return W
    if C < W:
        print('Error')
        return 0
    if C <= 2*W-1:
        return solve1(C-1, W-1) + 1
    # C >= 2W
    return max(solve1(2*(W-1), W-1), solve1(C-W, W)) + 1

def solve(R, C, W):
    return solve1(C, W) + (R-1)*int(C/W)

fin = open('A-large.in')
caseNum = int(fin.readline())
for caseNo in range(caseNum):
    R, C, W = map(int, fin.readline().strip().split())
    print('Case #%d: %d' % (caseNo+1, solve(R, C, W)))
fin.close()
