
def rev(R,k,N,L):
    total = 0
    while R>0:
        turn = 0
        K = []
        while L and turn+L[0]<=k:
            a = L.pop(0)
            K.append(a)
            turn += a
        total += turn
        L.extend(K)
        R -= 1
    return total


with open('C-small.in') as infile:
    T = int(infile.readline())
    with open('C-small.out','w') as outfile:
        j = 1
        while j<=T:
            R, k, N = tuple(map(int, infile.readline().split()))
            L = map(int, infile.readline().split())
            outfile.write('Case #%d: %s\n' %(j,rev(R,k,N,L)))
            j += 1
            
