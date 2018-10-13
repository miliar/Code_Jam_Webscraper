import sys
number = int(sys.stdin.readline().rstrip('\n'))

for i in range(number):
    l = sys.stdin.readline().rstrip('\n').split(' ')
    n = int(l[0])
    p = int(l[1]) + 1
    pp = pow(2, n)
    s = ""
    if (not (p % pp)):
        s = "ON"
    else:
        s = "OFF"
    print "Case #" + str(i+1) + ": " + s

