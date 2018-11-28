def flip(pan_str, side, num):

    pan = list(pan_str)
    # Left
    if(side == 0):
        for i in range(num):
            if(pan[i] == '+'):
                pan[i] = '-'
            else:
                pan[i] = '+'
    else:
        for i in range(num):
            if(pan[-1-i] == '+'):
                pan[-1-i] = '-'
            else:
                pan[-1-i] = '+'

    return ''.join(pan)


t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):

    inp = raw_input().split()
    # print inp
    D = int(inp[0])
    N = int(inp[1])
    horses = []
    for n in range(N):
        inp = raw_input().split()
        horses.append((D-int(inp[0]))/(int(inp[1])*1.0))

    slowest = max(horses)
    speed = D/slowest

    print "Case #{}: {}".format(i, speed)
