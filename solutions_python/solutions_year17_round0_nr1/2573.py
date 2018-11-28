'''
Created on Mar 19, 2016

@author: elmoatasem
'''

        
        
def flipSequence(seq):
    for i in range(len(seq)):
        if(seq[i] == '+'):
            seq[i] = '-'
        else:
            seq[i] = '+'
            
    return seq
    
    
def isFlipableSeq(seq):
    isFlippedSeq = False
    for i in range(len(seq)):
        if(seq[i] == '-'):
            isFlippedSeq = True
            break
        return isFlippedSeq
            
    return seq
    
    
    
def getNumberOfMinus(sequence):
    minusCount = 0
    for i in range(len(sequence)):
        if(sequence[i] == '-'):
            minusCount += 1
    return minusCount
    
    
    
def solve(pattern,K):
    
    pattern_list = list(pattern)
    happySequence = "+" * len(pattern)
    solved = False
    
    flips = 0
    firstSol = []
    while (True):       
        for j in range(len(pattern_list)):
            if(j + K < len(pattern_list) + 1): 
                subSeq = pattern_list[j:j+K]
#                 print subSeq

                if(isFlipableSeq(subSeq)):
                    pattern_list[j:j+K] = flipSequence(subSeq)
                    flips += 1
                    if(happySequence == "".join(pattern_list)):
                        solved = True
                        break
        if(happySequence == "".join(pattern_list)):
                solved = True
                break
        elif(getNumberOfMinus(pattern_list) == 1) :
                flips = -1
                break 
            
        if(len(firstSol) == 0): 
            firstSol = "".join(pattern_list)
        elif (firstSol == "".join(pattern_list)):
            
            flips = -1
            break 
            
            
#         print pattern_list,solved,flips
    return flips
    
    
    
    
    
    
            
f_r = open('A-large.in',"r")
# f_r = open('A-small-attempt0.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("A_Large.out", "w")
result = ""
for i in range(n_test):
    inputVal =  f_r.readline().strip().split()
    pattern = inputVal[0]
    K = int(inputVal[1])
#     print pattern,K
    flips = solve(pattern,K)
    if(flips == -1):
        result = "IMPOSSIBLE"
    else:
        result =  flips
    print pattern,K,result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()


