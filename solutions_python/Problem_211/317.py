


def solve(n,k,u,p):
    p.sort()
    index = 0
    while index < (len(p)-1) and p[index] == p[index-1]:
        index += 1
    #print("diff is " + str(p[index+1]-p[index]))
    while u > 0 and index+1 < len(p):
        diff = min(u,(index+1)*(p[index+1]-p[index]))
        inc = diff/(index+1)
        if index == 0:
            p[0] += inc

            u -= inc
        else:
            for i in range(index+1):
                p[i] += inc

                u -= inc
        index += 1

    if u > 0:
        inc = u/len(p)
        for a in range(len(p)):
            p[a] += inc
    sum = 1
    for a in p:
        sum *= a
    return str(round(sum,6))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    u = float(input().split(" ")[0])
    p = [float(s) for s in input().split(" ")]
    ans = solve(n,k,u,p)
    print("Case #{}: {}".format(i, ans))
    # check out .format's specification for more formatting options

