if __name__ == '__main__':
    openfile = open('C.in', 'r')
    T = int(openfile.readline()[:-1])
    for X in range(T):
        RkN = openfile.readline()
        R, k, N = [int(s) for s in RkN.split(' ')]
        groups_str = openfile.readline()
        group = [int(s) for s in groups_str.split(' ')]
        turn = 0
        euros = 0
        for j in range(R):
            people = 0
            start = turn
            while (group[turn] <= k - people):
                people += group[turn]
                turn += 1
                if turn == N:
                    turn = 0
                if turn == start:
                    break
            euros += people
        print 'Case #%s: %s' %(X+1, euros)

    openfile.close()
