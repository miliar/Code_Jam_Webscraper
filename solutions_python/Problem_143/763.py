from sys import argv
file = open(argv[1])
out = open("out.txt", "w")
cases = int(file.readline().strip("\n"))
num = 0
for case in xrange(cases):
    a, b, k = file.readline().strip("\n").split(" ")
    a, b, k = int(a), int(b), int(k)
    for x in xrange(a):
        for y in xrange(b):
            if (x&y)<k:
                num += 1
    out.write("Case #{}: {}\n" .format(case+1, num))
    num = 0