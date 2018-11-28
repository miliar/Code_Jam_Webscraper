T = int(input())

def solve(S):
    for j in range(len(S)-1):
        #Mismatch
        if S[j] > S[j+1]:
            #bound check
            if j > 0:
                if S[j-1] != S[j]:
                    return(S[:j] +[S[j]-1]+ [9]*(len(S)-j-1))
                else:
                    #find first mismatch
                    for k in range(j-1,-1,-1):
                        if S[k] != S[j]:
                            return(S[:k+1] + [S[k+1] - 1] +  [9]*(len(S)-k-2)) 
                    
                    return(S[:k] + [S[k] - 1] +  [9]*(len(S)-k-1)) 

            #First digit mismatches
            return [S[j] - 1] + [9]*(len(S)-1)
    #Already neat
    return S

for i in range(T):
    S = [int(x) for x in input()]
    print("Case #{}: {}".format(i+1, int("".join(str(x) for x in solve(S)))))