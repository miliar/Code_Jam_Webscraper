def solve(a, b):
    # a = max_shyness
    # b  = rest of line
    running_total = 0
    total_extra = 0

    for (shyness, people) in enumerate(b):
        if running_total >= shyness:
            running_total += people
        else:
            extra = shyness - running_total
            running_total += extra + people
            total_extra += extra
        #print running_total

    return total_extra

if __name__ == "__main__":
    count = int(raw_input())
    for i in xrange(count):
        line = raw_input()
        parts = line.split(" ")
        max_shyness = int(parts[0])
        counts = []
        for char in parts[1]:
            counts += [int(char)]
        solution = solve(max_shyness, counts)
        print "Case #%s: %s" % (i+1, solution)