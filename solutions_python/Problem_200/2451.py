
def isInOrder(s):
    last = "0"
    for c in str(s):
        if ord(c) >= ord(last):
            last = c
        else:
            return False
    return True


def solve(k):
    ans = str(k)
    for i in range(len(ans)-1, -1, -1):
        if isInOrder(ans):
            return int(ans)
        else:
            ans = str(int(ans) - (int(ans[i])+1)*10**(len(ans)-i-1))
    return int(ans)

# a long solution to verify results against short solution
def solve_long(k):
    for i in range(k,0,-1):
        last = "0"
        complete = isInOrder(str(i))
        if complete:
            return i
    return 0

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    ans = solve(int(k[0]))
    print("Case #{}: {}".format(i, ans))
    # check out .format's specification for more formatting options

