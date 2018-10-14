# Tidy Numbers

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inp = raw_input()
    small = int(inp[0])
    ind = 1
    smstart = 0
    ans = inp[0]
    while ind < len(inp):
        num = int(inp[ind])
        if small < num:
            small = num
            smstart = ind
            ans = inp[0:ind+1]
            ind += 1
        elif small == num:
            ans = inp[0:ind+1]
            ind += 1
        elif small > num:
            ans = ans[0:smstart] + str(small-1) + "9"*(len(inp)-smstart-1)
            ind = len(inp)

    ans = int(ans)
    print "Case #{}: {}".format(i, ans)
