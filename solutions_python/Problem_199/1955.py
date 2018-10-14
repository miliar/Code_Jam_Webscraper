import sys

def numFlips(S, K):
    '''returns the number of iterations or -1 '''
    S = str(S)
    iterations = 0
    for i in range(len(S)- K + 1):
        if S[i] == '-':
            #make a numFlips
            iterations += 1
            S = S[:i] + S[i:i+K].replace('+', '*').replace('-', '+').replace('*', '-') + S[i+K:]

    if '-' in S:
        return -1
    else:
        return iterations

def numFlips2(S, K, index = 0, it = 0):
    '''returns the number of iterations or -1 '''
    
    if '-' not in S:
        return it
    elif index + K > len(S):
        return -1
    else:
        #do the flip at index
        T = S[:index] + S[index:index+K].replace('+', '*').replace('-', '+').replace('*', '-') + S[index+K:]
       
        num1 = numFlips2(S, K, index+1, it)
        num2 = numFlips2(T, K, index+1, it+1)
        
        if num1*num2 >= 0 and (num1, num2) != (-1, -1):
            return it + min(num1, num2)
        else:
            return max(num1, num2)
    
    
        

f = open(sys.argv[1])
T = int(f.readline())

for i in range(T):
    S, K = f.readline().strip().split()
    K = int(K)
    result = numFlips(S, K)

    if result > -1:
        print("Case #{0}: {1}".format(i+1, result))
    else:
        print("Case #{0}: IMPOSSIBLE".format(i+1))

f.close()
