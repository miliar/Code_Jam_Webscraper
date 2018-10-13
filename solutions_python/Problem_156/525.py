def greatestDivisor(k):
    i = 2
    while i <= k/2:
        if k%i == 0:
            return k/i
        i+=1
    return -1

def min_minutes_print(P):
    print P
    nextP = [x-1 for x in P if x > 1]
    if(len(nextP) == 0):
        return 1
    Pmax = P[0]
    g = greatestDivisor(Pmax)
    if g == -1:
        P.append(Pmax/2)
        P[0] = (Pmax+1)/2
    else:
        P.append(g)
        P[0] = Pmax - g
    P.sort(None, None, True)
    print str(nextP) + ' or ' + str(P)
    return 1 + min(min_minutes(nextP), min_minutes(P))

def min_minutes(P):
    nextP = [x-1 for x in P if x > 1]
    if(len(nextP) == 0):
        return 1
    Pmax = P[0]
    g = greatestDivisor(Pmax) 
    if g == -1:
        P.append(Pmax/2)
        P[0] = (Pmax+1)/2
    else:
        P.append(g)
        P[0] = Pmax - g
    P.sort(None, None, True)
    return 1 + min(min_minutes(nextP), min_minutes(P))

if __name__ == '__main__':
    f = open('B-small-attempt5.in', 'r')
    o = open('B-small-attempt5.out', 'w')

    T = int(f.readline().strip())
    
    for i in range(1, T + 1):
        D = int(f.readline().strip().split()[0])
        P = map(int, f.readline().strip().split())
        P.sort(None, None, True)
        o.write('Case #' + str(i) + ': ' + str(min_minutes(P)) + '\n')