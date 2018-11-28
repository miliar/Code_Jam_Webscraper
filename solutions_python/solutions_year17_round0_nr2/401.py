def check(s):
    for i in range(1,len(s)):
        if s[i]<s[i-1]:
            return False
    return True

def converse(s):
    k = 0
    for i in range(1,len(s)):
            if s[i]<s[i-1]:
                k = i
                break
    if k > 0:
        s = s[:i-1]+str(int(s[i-1])-1)+'9'*(len(s)-i)
 #       print(k,s)
        s = converse(s)
        while s[0]=='0': 
            s = s[1:]    
    return(s)
T = int(input())
for t in range(1,T+1):
    s = input()
    s = converse(s)
    print('Case #'+str(t)+':', s)

        
        