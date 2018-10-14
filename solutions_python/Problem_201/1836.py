import sys

sys.stdout = open("./output.txt", "w")

t = int(input())
for i in range(1, t + 1):
    bigchunk, peoplenum = [int(s) for s in raw_input().split(" ")]
    totalchunks = [bigchunk]
    mx = mn = 0
    for j in range(1, peoplenum + 1):
        if bigchunk <= 1:
            mx = mn = 0
        else:
            if bigchunk % 2 == 0:
                mx = bigchunk / 2
                mn = mx - 1
            else:
                mx = mn = bigchunk / 2
            totalchunks.append(mx)
            totalchunks.append(mn)
            totalchunks.remove(bigchunk)
        bigchunk = max(totalchunks)

    print("Case #{}: {} {}".format(i,mx,mn))
