import sys
f = sys.stdin.readlines()
t = int(f[0])

f = [x.split() for x in f[1:]]
f = [(int(x[0]), [int(d) for d in x[1]]) for x in f]
case = 1
for smax, shyness in f:
    clappers = 0
    required = 0
    for i, s in enumerate(shyness):
        if clappers >= i:
            clappers += s
        else :
            required += i - clappers
            clappers = i + s
    print "Case #{0}: ".format(case) + str(required)
    case += 1
