def LsRs(stalls):   
    Ls = [None]*len(stalls)
    Rs = [None]*len(stalls)
    for i in range(len(stalls)):
        if stalls[i] == 1:
            Ls[i] = -1
            Rs[i] = -1
        else:
            ls = 0
            j = i-1
            while not stalls[j] == 1 and j > 0:
                ls +=1
                j -=1
            Ls[i] = ls

            rs = 0
            j = i+1
            while not stalls[j] == 1 and j < len(stalls):
                rs +=1
                j +=1
            Rs[i] = rs
    return Ls, Rs
    

def findstall(min_LsRs, max_LsRs):
    max_minspace = -1
    indices = []
    maxspace_for_best = []
    for i in range(len(min_LsRs)):
        if min_LsRs[i] > max_minspace:
            max_minspace = min_LsRs[i]
            indices = [i]
            maxspace_for_best = [max_LsRs[i]]
        elif min_LsRs[i] == max_minspace:
            indices.append(i)
            maxspace_for_best.append(max_LsRs[i])
    
#    print("indices:", indices)
#    print("maxspace_for_best:", maxspace_for_best)

    if len(indices) == 1:
        choice = indices[0]
    else:
        val = max(maxspace_for_best)
        # find first occurrence
        for i in range(len(maxspace_for_best)):
            if maxspace_for_best[i] == val:
                m_ind = i
                break       
        choice = indices[m_ind]
    return choice


def solution(N, K):

    #N = 10
    #K = 3

    stalls = [1] + [0]*N +[1]
#    print("Stalls: ", stalls)
    # Keep track of Ls and Rs for each stall and then update it for each person?
    # -1 if occupied

    # Ls = number of empty stalls to the left of this stall
    # Rs = number of empty stalls to the right of this stall
    Ls, Rs = LsRs(stalls)
#    print(Ls)
#    print(Rs)
#    print()

    # Starting min(Ls, Rs)
    min_LsRs = [min(Ls[i], Rs[i]) for i in range(len(Ls))]
    max_LsRs = [max(Ls[i], Rs[i]) for i in range(len(Ls))]
#    print("min_LsRs:", min_LsRs)
#    print("max_LsRs:", max_LsRs)
#    print()

    for i in range(K):
        min_LsRs = [min(Ls[i], Rs[i]) for i in range(len(Ls))]
        max_LsRs = [max(Ls[i], Rs[i]) for i in range(len(Ls))]

        choice = findstall(min_LsRs, max_LsRs)
        stalls[choice] = 1
        Ls, Rs = LsRs(stalls)
        
#        print("Choice: ", choice)
#        print("Stalls: ", stalls)
#        print()
        
#    print("min_LsRs:", min_LsRs)
#    print("max_LsRs:", max_LsRs)
#    print()
    
    return max_LsRs[choice], min_LsRs[choice]

N = 6
K = 2
max_lsrs, min_lsrs = solution(N,K)  

# Read input
nT = int(input())  # read a line with a single integer
N = [None]*nT
K = [None]*nT
for i in range(nT):
    n,k = input().split() # read a single integer
    N[i] = int(n)
    K[i] = int(k)

#print(N)
#print(K)

res = [None]*nT
for i in range(nT):
    ls, rs = solution(N[i], K[i])   
    #print((ls,rs))
    print('Case #' + str(i+1) + ": " + str(ls) + " " + str(rs))
#    
#for i in range(1,len(res)+1):
#    print('Case #' + str(i) + ": " + str(res[i-1]))
