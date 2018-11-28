c = int(raw_input())
def rotate(val, low, up):
    count = 0
    cur = val/10 + (val%10) * 10 ** (len(str(val))-1)
    while cur != val:
        if (cur > val) and cur <= up:
            count = count + 1
        cur = cur/10 + (cur%10) * 10 ** (len(str(val))-1)
    return count


for i in range(c):
    data = raw_input().split()
    low = int(data[0])
    up = int(data[1])
    count = 0
    for val in range(low, up+1):
        count = count + rotate(val, low, up)
    print "Case #%d: %d" % (i+1, count)

