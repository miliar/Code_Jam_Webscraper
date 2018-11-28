from sys import stdin


def solve(sMax, line):
    minPeople = 0
    count = 0
    # print line, type(line)4 11111
    for i in range(len(line)):
        d = int(line[i])
        if i == 0:
            count = d
        else:
            if count < i:
                minPeople += i - count
                count += i - count
                count += d
            else:
                count += d

        # print "MP ",minPeople, "count", count, "i=",line[i]
    return minPeople
inp = stdin.readline()
T = int(inp)
# print "T",T
# T=1
for t in range(T):
    inp = str(stdin.readline())
    print "Case #" + str(t+1) + ": " + str(solve(int(inp.split()[0]), inp.split()[1]))