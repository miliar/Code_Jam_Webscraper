import sys

def Ls(stalls, index):
    count = 0
    while index > 0 and stalls[index-1] == '.':
        count += 1
        index -= 1
    return count

def Rs(stalls, index):
    count = 0
    l = len(stalls)
    while index < l-1 and stalls[index+1] == '.':
        count += 1
        index += 1
    return count


def find_empty(S):
    '''returns a list of indexes'''
    index = 0
    while True:
        index = S.find('.', index)
        if index == -1:
            return
        yield index
        index += 1


def computeStalls(N, K):
    S = '.'*N 
    for i in range(K):
        indexes = list(find_empty(S))
        ls, rs, position = (0, 0, -1)
        for index in indexes:
            currentLs = Ls(S, index)
            currentRs = Rs(S, index)
            if min(currentLs, currentRs) >= min (ls, rs):
               if not((min(currentLs, currentRs) == min(ls, rs)) and(max(currentLs, currentRs) <= max(ls, rs))):
                    ls, rs, position = (currentLs, currentRs, index)
        print(S)
        S = S[:position] + '0' + S[position+1:]
    return (max(ls, rs), min(ls, rs))

def computeStalls2(N, K):
    S =  '.'*N 
    #initialize 
    distances = []
    for i in range(N):
        # (Ls, Rs)
        distances.append((i, N-i-1))
    for i in range(K):
        indexes = list(find_empty(S))
        ls, rs, position = (0, 0, -1)
        modified = False
       
        for index in indexes:
            if min(distances[index]) >= min(ls, rs):
                if not ((min(distances[index]) == min(ls, rs)) and(max(distances[index]) <= max(ls, rs))):
                    ls, rs = distances[index]
                    position = index
                    modified = True
        if modified:
            j = position-1
            while j >=0 and S[j] == '.':
                distances[j] = (distances[j][0], position-1 -j)
                j -= 1

            j = position + 1
            while j < N and S[j] == '.':
                distances[j] = (j - position - 1, distances[j][1])
                j += 1
        
            
        

            if (position > 0) and (position < N-1) and ('0' != S[position-1]) and ('0' != S[position+1]):
                distances[position] = (distances[position-1][0] +1, distances[position+1][1] + 1)
            elif (position > 0) and ('0' != S[position-1]):
                distances[position] = (distances[position-1][0] +1, 0)
            elif (position < N-1) and ('0' != S[position+1]):
                distances[position] = (0, distances[position-1][1] +1)
            else:
                distances[position] = (0, 0)
            
            S = S[:position] + '0' + S[position+1:]

    return (max(ls, rs), min(ls, rs))
        
            

f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    N, K = f.readline().strip().split()
    N, K = (int(N),  int(K))
   
    result = computeStalls2(N, K)
    
    print("Case #{0}: {1} {2}".format(i+1, result[0], result[1]))
f.close()



