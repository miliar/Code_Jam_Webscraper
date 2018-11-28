def solve(R, C, M):
    """ solve the problem """

    #print(R, C, M)

    count = 0
    for i in range(R):
        for j in range(C):
            #print('wew', M, i, j)
            #print(i, j)
            if M[i][j] == '.': continue

            isok = False

            if M[i][j] == '>':
                for k in range(j+1, C):
                    if M[i][k] != '.':
                        isok = True
                        break
            if isok: continue

            if M[i][j] == '<':
                for k in range(0, j):
                    if M[i][k] != '.':
                        isok = True
                        break
            if isok: continue

            if M[i][j] == '^':
                for k in range(0, i):
                    if M[k][j] != '.':
                        isok = True
                        break
            if isok: continue

            if M[i][j] == 'v':
                for k in range(i+1, R):
                    if M[k][j] != '.':
                        isok = True
                        break
            if isok: continue
            #print('notfound')

            
            isfound = False
            for ii in range(R):
                if ii==i: continue
                if M[ii][j] != '.':
                    isfound = True
                    break
            for jj in range(C):
                if jj == j: continue
                if M[i][jj]!= '.':
                    isfound = True
                    break

            if isfound:
                count += 1
            else:
                return 'IMPOSSIBLE'



    return count


def parse():
    """ parse input """

    R, C = [int(i) for i in input().split()]
    M = []
    for i in range(R):
        #M.append([i for i in input().split()])
        M.append(input())

    return R, C, M


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
