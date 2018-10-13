def is_tidy(n):
    n = str(n)
    n = list(n)
    if len(n) == 1:
        return True
    for i in range(0,len(n)-1):
        if n[i + 1] < n[i]:
            return False
    return True


t = int(raw_input())
for i in range(0,t):

    
    n = list(raw_input())
    for j in range(len(n)-2,-1,-1):
        
        q = int(''.join(n[j:]))
        
        if is_tidy(q):
            continue
        
        else:
            n[j] = str(int(n[j]) - 1)
            for k in range(j+1,len(n)):
                n[k] = '9'
    if n[0] == '0':
        del n[0]
    print "Case #" + str(i+1) + ": " + ''.join(n)
