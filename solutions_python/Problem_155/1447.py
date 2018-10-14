n =  int(input())
out = open("c:/ws/codejam/a.out", "w")
for j in range(n):
    arr = input().split(" ")[1]
    fr, csum = 0, 0
    i = 0
    for c in arr:
        if (i > csum):
            fr += (i - csum)
            csum += (i - csum)
        csum += int(c)
        i += 1
    out.write("Case #%d: %d" % (j + 1, fr) + "\n")
out.close()