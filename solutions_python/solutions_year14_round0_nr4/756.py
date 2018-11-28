from random import randint




def fair_war (N, K):
    '''N and K are lists of masses'''
    naomi_score = 0
    N.sort()
    K.sort()
    while N and K:
        length = len(N)
        r = randint(0, length - 1)
        elem = N.pop(r)
        if elem > K[-1]:
            naomi_score += 1
            K = K[1:]
        elif elem < K[0]:
            K = K[1:]
        else:
            i = 0
            while i < length:
                if K[i] > elem:
                    K.pop(i)
                    break
                i += 1
            if i == length:
                naomi_score += 1
                K = K[1:]
    return naomi_score

 
        
        


def deceitful_war (N, K):
    '''N and K are lists of masses'''
    N.sort()
    K.sort()
    naomi_score = 0
    while N and K:
        length = len(N)
        if length == 1:
            told = N[0]
            if told > K[0]:
                naomi_score += 1
            return naomi_score
        if N[0] > K[0]:
            told = K[-1] + 0.1
            K, N = K[1:], N[1:]
            naomi_score += 1
        elif N[0] < K[0]:
            told = (K[-1] + K[-2]) / 2
            K, N = K[:-1], N[1:]
    return naomi_score            
        
            
f = open ('warLargeIN.in', 'r')
g = open ('warLargeOUT.txt','w')
numCases = int(f.readline())
for case in xrange (1, numCases + 1):
    f.readline() #the number of blocks each player has
    line1 = f.readline().split()
    line2 = f.readline().split()
    Naomi = map (lambda x: float(x), line1)
    Ken = map (lambda x: float(x), line2)
    g.write ('Case #' + str(case) + ': ' + str(deceitful_war (Naomi, Ken)) +\
             ' ' + str(fair_war(Naomi, Ken)) + '\n')
g.close()
f.close()