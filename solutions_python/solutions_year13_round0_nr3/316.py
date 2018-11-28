## compute table of all fair numbers 1..1e7
def isPalindrome(x):
    s = str(x)
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return False
    return True

def computeTable(N):
    res = []
    for x in range(1,N+1):
        if isPalindrome(x):
            if isPalindrome(x*x):
                res.append(x*x)
    return res
                

def solve(A,B,table):
    return sum([int(A<=item<=B) for item in table]) 
                    
##            
## MAIN PROGRAMM
##
table = computeTable(10000000)

T = int(input())
for t in range(T):
    ## read case
    A, B = map(int, input().rstrip().split())
        
    ## solve and print results
    result = solve(A,B,table)
    print('Case #'+str(t+1)+': '+str(result))

    
