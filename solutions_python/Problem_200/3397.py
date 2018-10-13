T = int(input())
for c in range(T):
    s = list(input())
    for i in range(len(s)-1):
        j=len(s)-1-i
        if int(s[j-1]) > int(s[j]):
            for k in range(j, len(s)):
                s[k] = '9'
            s[j-1] = str(int(s[j-1])-1)
    print ("Case #"+str(c+1)+": "+str(int(''.join(s))))

