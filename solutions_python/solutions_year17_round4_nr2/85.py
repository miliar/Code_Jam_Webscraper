from collections import Counter
def solve(N, C, M, P, B):
    """ solve the problem """

    #print(N, C, M, P, B)
    if C == 2:
        t1 = []
        t2 = []
        for i in range(M):
            if B[i] == 1: t1.append(P[i])
            elif B[i] == 2: t2.append(P[i])
            else: 0/0
        if len(t1) > len(t2):
            t1, t2 = t2, t1
        c1 = Counter(t1)
        c2 = Counter(t2)
        #print(c1, c2)
        n_same = 0
        pos_same = -1
        for i in range(1, N+1):
            s = min(c1[i], c2[i])
            if s >= n_same: 
                n_same = s
                pos_same = i
        #print(c1, c2, n_same, pos_same)
        if pos_same == -1:
            return len(t2), 0
        elif pos_same == 1:
            c2_remain = len(t2) - c2[pos_same]
            c1_need = c1[pos_same] - c2_remain 
            c1_need = max(c1_need, 0)
            return len(t2) + c1_need, 0
        else: 
            c2_remain = len(t2) - c2[pos_same]
            c1_need = c1[pos_same] - c2_remain 
            c1_need = max(c1_need, 0)
            return len(t2), c1_need
            
    return 


def parse():
    """ parse input """
    N, C, M = [int(i) for i in input().split()]
    P = []
    B = []
    for m in range(M):
        p, b = [int(i) for i in input().split()]
        P.append(p)
        B.append(b)


    return N, C, M, P, B


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        #if t != 4: continue
        result = solve(*params)
        if result != None:
            print('Case #%d: %s %s' % (t, result[0], result[1]))


if __name__ == '__main__':

    main()
