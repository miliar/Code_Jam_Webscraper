data = open("inputB.txt")
output = open("outputB3.txt", "w")
debug = open("debug.txt", "w")
T = int(data.readline())
for t in range(T):
    debug.write("Processing case #%d\n" % (t+1,))
    D = int(data.readline())
    counts = [int(x) for x in data.readline().split()]
    debug.write("Starting point is D = %d and counts = %s\n" %(D, str(counts)))
    lowest_found = max(counts)
    penalty = 2
    while penalty < lowest_found:
        total = 0
        for plate in counts:
            total += ((plate - 1) // penalty)
        lowest_found = min(lowest_found, total + penalty)
        penalty += 1
    output.write("Case #%d: %d\n" % (t+1, lowest_found))
output.close()
debug.close()
