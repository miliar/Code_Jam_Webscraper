# Problem B

# Small dataset
# O = G = V = 0. (Each unicorn has only one hair color in its mane.)

def solve(N, R, Y, B):
    res = ""
    imp = "IMPOSSIBLE "

    if sum((R,Y,B)) == 0:
        return ""

    if max(R,Y,B) > N//2 :
        return imp

    if (R==Y) and (Y==B):
        return "RYB"*R
    elif (R==Y) and (B == 0):
        return "RY"*R
    elif (R==B) and (Y == 0) :
        return "RB"*R
    elif (Y==B) and (R == 0) :
        return "YB"*Y


    arr = [["R",R],["Y",Y],["B",B]]
    arr.sort(key=lambda x:x[1], reverse=True)

    sum_arr = lambda x : x[0][1] + x[1][1] + x[2][1]

    while(sum_arr(arr) > 0 ):
        if (arr[0][1] == arr[1][1]) and (arr[1][1] == arr[2][1]):
            m = arr[0][1]
            s = set(["B","R","Y"])
            s.remove(res[-1])
            first = min(s)
            s.add(res[-1])

            s.remove(first)
            s.difference_update(set([res[0]]))
            last = min(s)
            s = set(["B","R","Y"])
            s.remove(first)
            s.remove(last)
            mid = list(s)[0]

            r0 = first+mid+last
            r = r0*m
            res += r
            break
        if arr[0][1] > 0:
            res += arr[0][0]
            arr[0][1] -= 1
        if arr[1][1] > 0 :
            res += arr[1][0]
            arr[1][1] -= 1

        arr.sort(key=lambda x:x[1], reverse=True)

    return res


if __name__ == "__main__":
    tc = int(input())
    for ti in range(tc):
        N, R, O, Y, G, B, V = map(int,input().strip().split())
        r = solve(N, R, Y, B)
        print("Case #{0}: {1}".format(ti + 1, r))
