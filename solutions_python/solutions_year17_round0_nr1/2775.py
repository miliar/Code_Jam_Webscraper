t = input()
for pappu in range(t):
    n,k = raw_input().split()
    n = list(n)
    k = int(k)
    lst = []
    cm = 0
    ans = 0
    for i in range(len(n)):
        if n[i] == '-':
            cm += 1
    while cm:
        ans += 1
        i = 0
        while i < len(n):
            if n[i] == '-':
                for j in range(k):
                    if i+j >= len(n):
                        ans = 'IMPOSSIBLE'
                        break
                    if n[i+j] == '-':
                        n[i+j] = '+'
                        cm -= 1
                    else:
                        n[i+j] = '-'
                        cm += 1
                    
                if ans == 'IMPOSSIBLE':
                    break
                
                i = len(n)
            i += 1
            
        if ans == 'IMPOSSIBLE':
            break
 
    print "Case #" + str(pappu+1) + ": " + str(ans)
    
        
    
