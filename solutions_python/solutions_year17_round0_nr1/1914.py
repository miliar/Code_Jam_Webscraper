def flip(s, k):
    count = 0
    sl = [c for c in s]
    for i in range(0, len(sl) - k + 1):
        if sl[i] == "-":
            count += 1
            for x in range(i, i+k):
                sl[x] = "+" if sl[x] == "-" else "-"
    for z in sl:
        if z == "-":
            return "IMPOSSIBLE"
    return count

t = int(input())
for i in range(1,t+1):
    s, k = input().split(" ")
    k = int(k)
    print("Case #{}: {}".format(i, flip(s, k)))
