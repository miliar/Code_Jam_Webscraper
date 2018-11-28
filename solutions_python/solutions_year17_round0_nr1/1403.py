


def rotate(K,S):
    #K is rotator size
    #S is string
    S = list(S)
    rotates = 0
    for pos,pancake in enumerate(S):
        if(pos + K  > len(S)):
            break
        if(pancake == '-'):
            #Flip K pancaces
            for i in range(K):
                if(S[i + pos] == '-'):
                    S[i + pos] = '+'
                else:
                    S[i + pos] = '-'
            pos = pos + K
            rotates += 1 
    if('-' in S):
        rotates = 'IMPOSSIBLE'
    return S, rotates

if __name__ == "__main__":
    import sys
    file = sys.argv[1]
    try:
        file = open(file,'r')
    except IOError:
        print("Can't open file")

    T = int(file.readline().rstrip())
    for i in range(T):
        S, K = file.readline().rstrip().split(' ')
        K = int(K)
        print("Case #{0}: {1}".format(i+1,rotate(K,S)[1]) )
