fileHandle = open('in.txt', 'r')
#outputHandle = open('out.txt', 'w')


def base_time(c, f, n):
    time = 0
    for i in range(n):
        time += c/(2.0+i*f)
    return time


def try_min_time(c, f, x):
    previous_time = x/2
    n = 1

    while True:
        current_time = x/(2+n*f) + base_time(c, f, n)
        if current_time > previous_time:
            return previous_time
        previous_time = current_time
        n += 1

caseNumber = int(fileHandle.readline())

for i in range(caseNumber):
    [c, f, x] = [float(j) for j in fileHandle.readline().split(" ")]
    print "Case #" + str(i+1) + ": %.7f"%try_min_time(c, f, x)

fileHandle.close()