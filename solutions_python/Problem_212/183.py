import sys

stdout = sys.stdout
stdin = sys.stdin
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def solve():
    N, P = map(int, input().split())
    Gs = list(map(lambda x: int(x)%P, input().split()))
    total = len(Gs)
    nums = [0, 0, 0, 0]
    for G in Gs:
        nums[G] += 1
    ans = nums[0]
    used = 0
    if P == 2:
        pairs = nums[1]//2
        used += pairs*2
    if P == 3:
        pairs1 = min(nums[1], nums[2])
        pairs2 = (nums[1]-pairs1)//3
        pairs3 = (nums[2]-pairs1)//3
        #print(pairs1, pairs2, pairs3)
        pairs = pairs1 + pairs2 + pairs3
        used += pairs1*2 + pairs2*3 + pairs3*3
    if P == 4:
        pairs1 = min(nums[3], nums[1])
        pairs4 = nums[2]//2
        pairs2 = min(nums[2]-2*pairs4, (nums[1]-pairs1)//2)
        pairs6 = min((nums[3]-pairs1)//2, nums[2]-2*pairs4-pairs2)
        pairs3 = (nums[1]-pairs1-2*pairs2)//4
        pairs5 = (nums[3]-pairs1)//4
        pairs = pairs1 + pairs2 + pairs3 + pairs4 + pairs5
        used += pairs1*2 + pairs2*3 + pairs3*4 + pairs4*2 + pairs5*4

    if ans + used < total:
        ans += 1
    ans += pairs

    return ans

T = int(input())
for CASE in range(1,T+1):
    print('Case #' + str(CASE) + ': ', end='')
    print(solve())

sys.stdout = stdout
sys.stdin = stdin
