import fileinput

def solve(counts):
    standers = 0
    result = 0
    for c in xrange(len(counts)):
        people = counts[c]
        if c > standers:
            needed = (c - standers)
            standers += (people + needed)
            result += needed
        else:
            standers += people
    return result

lines = fileinput.input()
cases = lines.next()

n = 1
for line in lines:
    data = line.split()
    max_shyness = int(data[0])
    counts = [int(x) for x in data[1]]
    print "Case #" + str(n) + ": " + str(solve(counts))
    n += 1
