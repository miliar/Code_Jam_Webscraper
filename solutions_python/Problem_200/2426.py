

t = int(raw_input())



def solve(x):
    # x list of digits
    j = len(x) - 1
    while j > 0:
        ahead = x[j - 1]
        current = x[j]

        if int(ahead) > int(current) or current == "0":
            for idx in xrange(j, len(x)):
                x[idx] = "9"
            if ahead != "0":
                x[j - 1] = str(int(ahead) - 1)
        j -= 1

    return int("".join(x))



for i in xrange(t):
    x = list(raw_input())
    print "Case #" + str(i + 1) + ": " + str(solve(x))