t = int(input())
for i in range(t):
    n = (input())
    m = list(n)
    count = 0
    while(True):
        if(sorted(m) == m):
            print("Case #%d: %s" %(i+1,"".join(m).strip('0')))
            break;
        else:
            m[-1-count] = '9'
            p = int("".join(m[:-1-count]))
            p-=1
            m[:-1-count] = list(str(p))
            count+=1
        
