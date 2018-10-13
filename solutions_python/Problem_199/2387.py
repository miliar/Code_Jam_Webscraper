t=input()
for i in range(int(t)):
    si,k=(input().split())
    s = list(si)
    #print(len(s))
    c=0
    for j in range(len(s)):
        if s[j] == '-':
            
            if j+int(k) <= len(s):
                c+=1
                for l in range(int(k)):
                
                    if s[j+l]=='-':
                        s[j+l]='+'
                    else:
                        s[j+l]='-'
    #print(s)            
    if '-' in s:
        print("Case #"+str(i+1)+": "+"IMPOSSIBLE")
    else:
        print("Case #"+str(i+1)+": "+str(c))
