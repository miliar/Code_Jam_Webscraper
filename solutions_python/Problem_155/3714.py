f = open("A-small-attempt2.in", "r")
output = open("opera_output.txt", "w")
T = int(f.readline())
for testcase in range(T):
    line = f.readline().strip('\n')[2:]
    currStanding = 0
    needed = 0

    for s in range(len(line)):
        if s - currStanding > 0:
            needed += s - currStanding
            currStanding += s - currStanding
        currStanding += int(line[s])

    output.write("Case #%d: %d\n" % ( testcase+1, needed))

f.close()
output.close()
