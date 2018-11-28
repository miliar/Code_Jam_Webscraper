# snapper

# read input file
fIn = open("input.txt")

# get count
count = int(fIn.readline())

# read each line
for i in range(count):
    line = fIn.readline().split(' ')
    N = int(line[0])
    K = int(line[1])

    # make snapper chain
    snappers = [False for j in range(N)]

    for j in range(K):
        # the first one always has power and therefore always flips
        previous = True
        # flip the chain of snappers until we hit one which was previously off
        for k in range(N):
            if not previous:
                break
            previous = snappers[k]
            snappers[k] = not snappers[k]

    print "Case #{case}: {state}".format(case=i+1, state="ON" if all(snappers) else "OFF")


