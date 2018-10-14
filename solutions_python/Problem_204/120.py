def solve(N, P, R, Q):
    """ solve the problem """

    # Q[i][j] = the j-th package of ingre i-th  

    C = []

    #print(N, P, R, Q)
    for i in range(N):
        Q[i].sort(reverse=True)


    for i in range(N):
        for j in range(P):
            C.append([])
            #C[i][j] = []
            #big = int(0.0000000001 + Q[i][j] * 100 / R[i] / 90)
            #small = -round( - Q[i][j] * 100 / R[i] / 110)
            #if big >= 0:
            #    C[i].append( (big, small) )

            big = int(0.00000001+Q[i][j] * 10 / 9 / R[i])
            small = int( 0.99999999 +  Q[i][j] * 10 / 11 / R[i])
            #print(Q[i][j] * 10 / 9 / R[i])
            #print(Q[i][j] * 10 / 11 / R[i])
            #print(big, small)

            C[i].append( (big, small) )
            if False:
                b = int(0.0000001 + Q[i][j]  / R[i] )
                l = []
                big = b
                while True:
                    if big == 0:
                        big += 1 
                        continue
                    if big * R[i] * 0.9 <= Q[i][j] <= big * R[i] * 1.1: 
                        l.append(big)
                        big += 1
                    else: break
                small = b
                while True:
                    if small == 0: break
                    if small * R[i] * 0.9 <= Q[i][j] <= small * R[i] * 1.1: 
                        l.append(small) 
                        small -= 1
                        if small == 0: break
                    else: break
                if len(l) > 0:
                    #print(l)
                    C[i].append( ( max(l), min(l) ) )
    #print(C)

    count = 0
    while True:
        #print('V')
        g = False
        for i in range(N):
            if len(C[i]) == 0: 
                g = True
                break
        if g: break

        l = []        
        for i in range(N):
            #print('v', C[i])
            l.append(C[i][0][0])
            l.append(C[i][0][1])
        l.sort(reverse=True)
        done = False
        for s in l:
            ok = True
            for i in range(N):
                if C[i][0][0] >= s >= C[i][0][1]:
                    pass
                else:
                    ok = False
                    break
            if ok: 
                done = True
                break

        if done:
            count += 1
            for i in range(N):
                C[i].pop(0)
        else:
            min_big = 10000000
            for i in range(N):
                min_big = min(min_big, C[i][0][0])
            for i in range(N):
                if C[i][0][1] > min_big: C[i].pop(0)

    return count


def parse():
    """ parse input """

    N, P = [int(i) for i in input().split()]
    R = [int(i) for i in input().split()]
    Q = []
    for i in range(N):
        q = [int(i) for i in input().split()]
        Q.append(q)

    return N, P, R, Q


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        #if t != 93: continue
        #if t != 5: continue
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
