def solve(shynesses):
    standing = 0
    invites = 0
    for required, num in enumerate(shynesses):
        invites += max(required - (standing + invites), 0)
        standing += num
    return invites

T = int(raw_input())
for i in range(T):
    [_, shynesses] = raw_input().split()
    ans = solve(map(int, shynesses))
    print "Case #{}: {}".format(i + 1, ans)

