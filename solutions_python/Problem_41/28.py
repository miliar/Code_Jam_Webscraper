'''
Created on Sep 12, 2009

@author: AliJ
'''

def parse_num():
    return map(int, raw_input().split())



def process_case():
    
    N = list(raw_input().strip())
    fixed = False
    
    for i in range(len(N)-1,0, -1):
        
        if N[i] > N[i-1]:
            fixed = True
            
            best = i
            for j in range(i+1, len(N)):
                if N[j] > N[i-1] and N[j] < N[i]:
                    best = j
                                
            temp = N[best]
            N[best] = N[i-1]
            N[i-1] = temp
            
            L = N[i:]
            L.sort()
            N[i:] = L
            
            break

    result = ""        
    if fixed:
        for i in range(len(N)):
            result = result + N[i]
    else:
        N.sort()
        j=0
        while N[j] == '0':
            j+=1
 
        result = N[j]
        N[j] = '0'
        for i in range(len(N)):
            result = result + N[i]    
    
    return result


numCases = int(raw_input())

for i in range(numCases):
            
    print "Case #"+str(i+1)+":", (process_case())