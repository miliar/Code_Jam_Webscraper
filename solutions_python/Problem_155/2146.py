__author__ = 'loi'
f = open("A-large.in", "r")
o = open("output.out", "w")



tests = int(f.readline())
for test in range(tests):
    line = f.readline().strip().split()
    sMax = int(line[0])
    additional = 0
    total = 0
    s = line[1]
    for i in range(sMax+1):
        if total < i:
            additional += i - total
            total += (i-total) + int(s[i])
        else:
            total += int(s[i])
    o.write("Case #" + str(test + 1) + ": " + str(additional) + "\n")