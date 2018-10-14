def node(n, k):
    mini = (n-1)//2
    maxi = (n-1)//2 + (n-1)%2
    # pick stall
    if k==1:
        return maxi, mini
    # calc relevant subtree
    k -= 1
    if k%2 == 1:
        return node(maxi, k//2 + k%2) #odd
    return node(mini, k/2) #even

for case in range(int(input())):
    n, k = map(int, input().split())
    maxi, mini = node(n, k)
    print("Case #%d: %d %d"%(case+1, maxi, mini))
