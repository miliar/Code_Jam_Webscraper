import operator

for x in range(int(raw_input())):
    a = int(raw_input())
    l = [int(i) for i in raw_input().split()]
    for i in range(len(l)):
        if not reduce(operator.xor, l):
            sol = str(sum(l) - min(l))
        else:
            sol = "NO"
    print "Case #" + str(x+1) + ": " + sol

