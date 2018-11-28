t = int(input())  # read a line with a single integer
ct = 0
count = 0
while t > 0:
    d, n = [int(s) for s in input().split(" ")]
    if count == 0:
        if ct > 0:
            print("Case #{}: {}".format(ct, (end/l)))
        count = n
        end = d
        ct += 1
        l = -1
        t += n - 1
    else:
        count -= 1
        if (end-d)/n > l:
            l = (end - d)/n
        t -= 1
print("Case #{}: {}".format(ct, end/l))
