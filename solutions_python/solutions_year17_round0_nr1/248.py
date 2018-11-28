# Oversized Pancake Flipper

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inp = raw_input().split(" ")
    s = inp[0]
    k = int(inp[1])
    solved = False
    num = 0
    imp = False
    while not solved and not imp:
        j = s.find("-")
        if j == -1:
            solved = True
        elif j + k > len(s):
            imp = True
        else:
            pos = j
            while j < pos + k:
                if s[j] == "-":
                    s = s[0:j] + "+" + s[j+1:]
                elif s[j] == "+":
                    s = s[0:j] + "-" + s[j + 1:]
                j += 1
            num += 1

    if imp == True:
        ans = "IMPOSSIBLE"
    else:
        ans = num
    print "Case #{}: {}".format(i, ans)