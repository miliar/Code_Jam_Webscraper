t = int(input())

def xor(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

for i in range(t):
    count = 0
    flag = 0
    s,k = input().split()
    s = s.replace('-','0')
    s = s.replace('+','1')
    #print(s)
    t = list(s)
    k = int(k)
    a = '1' * k
    #a = int(a)
    #print(a)
    while( True ):
        l = s.find('0')
        if(l == -1):
            break
        elif(l + k  <= len(s)):
            count += 1
            p = (s[l : l + k])
            #print(p)
            t[l:l + k] = (xor(p,a))
            #print(t)
            s = "".join(t)
            #print(s)
        else:
            flag = -1
            print("Case #%d: %s"%(i+1,"IMPOSSIBLE"))
            break;
    if(flag == 0):
        print("Case #%d: %d"%(i+1,count))
                
        
    
        
