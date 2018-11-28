
def solve2(n,k):

    mini = n / (2**k) - 1.0
    maxi = n / (2**k)

    mini_rest = mini - int(mini)
    maxi_rest = maxi - int(maxi)

    if mini_rest >= 0.5:
        mini = int(mini) + 1
        if mini_rest>0.5 and maxi_rest == 0.5:
            maxi = int(maxi) +1
        else:
            maxi = int(maxi)
    else:
        mini = int(mini)
        maxi = int(maxi)

    if mini < 0:
        mini = 0
    if maxi < 0:
        maxi = 0
    return max(mini,maxi), min(mini,maxi)

def solve(n,k):
    left = int((n-1)/2)
    right = n/2 if n%2==0 else left
    if k == 1:
        return right,left

    if k==2:
        return solve(right, 1)
    if (k-1)%2 == 0:
        return solve(left, (k-1)/2)
    else:
        return solve(right, k/2)



_T = int(input())

for _i in range(1, _T + 1):

    n,k = map(int,input().split(" "))

    maxi, mini = solve(n,k)
    print("Case #%d: %d %d" % (_i, maxi, mini))
