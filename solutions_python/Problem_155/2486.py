tests = int(raw_input())

for test in range(1, tests + 1):
    str_in = raw_input()
    n = int(str_in.split()[0])
    spectators = str_in.split()[1]
    spectators = [int(spec) for spec in spectators]
    needed = 0
    up = 0
    for i in range(len(spectators)):
        if i == 0:
            up += spectators[i]
        else:
            if up >= i:
                up += spectators[i]
            else:
                needed += i - up
                up += spectators[i] + i - up

    print 'Case #' + str(test) + ': ' + str(needed)
