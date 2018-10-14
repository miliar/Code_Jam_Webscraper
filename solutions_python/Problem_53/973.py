def change_state(state):
    # One snap has happened, change the state
    state[0][1] = not state[0][1]
    for i, snapper in enumerate(state[1:]):
        if snapper[0] == True:
            snapper[1] = not snapper[1]
        if state[i][0] == True and state[i][1] == True:
            snapper[0] = True
        else:
            snapper[0] = False
    return

def snapit(n, k):
    # Initialize states. The structure is for each snapper we
    # keep [Power receiving, On/Off state]. Snapper 0 is always
    # receiving power no matter what because it is always connected
    # to socket
    state = [[True, False]]
    for i in range(n-1):
        state.append([False, False])

    # Series of snaps
    for i in range(k):
        change_state(state)

    return 'ON' if state[-1][0] == True and state[-1][1] == True else 'OFF'


if __name__ == '__main__':
    ifile = open('A-small-attempt0.in')
    ofile = open('A-small-attempt0.out', 'w')
    ncases = int(ifile.readline())

    for i in range(ncases):
        test_case = ifile.readline().strip().split()
        n = int(test_case[0])
        k = int(test_case[1])
        ofile.write('Case #%d: %s\n' % (i + 1, snapit(n, k)))

