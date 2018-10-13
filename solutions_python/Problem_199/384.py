def flip(i):
    global s
    ss = ''
    for j in range(i,i+n):
        if s[j]=='-':
            ss = ss + '+'
        else:
            ss = ss + '-'
#    print(i,ss,s)    
    return ss
T = int(input())
for t in range(1,T+1):
    s, n = input().split()
    n = int(n)
    k = 0
    for i in range(len(s)-n+1):
        if s[i]=='-':
            k += 1
            ss = flip(i)
            s = s[:i] + ss + s[i+n:]
    if s.rfind('-') >= 0:
        print('Case #'+str(t)+':', 'IMPOSSIBLE')
    else:
        print('Case #'+str(t)+':', k)
        
        
        
        
        
        