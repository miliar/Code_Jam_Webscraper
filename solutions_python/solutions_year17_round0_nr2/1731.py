
def isTidy(n):
    """
        returns 0 if it is tidy
        else returns the number it can subtract
        safely to get to the next check
    """
    for i in range(0,len(n)-1):
        if n[i] > n[i+1]:
            return int(n[i+1::]) + 1
    return 0

def solve(x):
    while True:
        sub = isTidy(str(x))
        if sub == 0:
            return x
        x -= sub

N = int(input().strip())
for i in range(0, N):
    x = int(input().strip())
    result = solve(x)
    print("Case #{}: {}".format(i + 1, result))
