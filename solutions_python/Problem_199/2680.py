def flip(s, j, n):
    for k in range(n):
        if s[j+k]=='-':
            s[j+k]='+'
        else:
            s[j+k]='-'
    return s

for i in range(input()):
    s,n = raw_input().split(' ')
    n = int(n)
    s = list(s)
    c=0
    for j in range(len(s)-n+1):
        if s[j]=='-':
            s = flip(s,j,n)
            c+=1
    if s.count('-')==0:
        print ("Case #" + str(i+1) + ": " + str(c))
    else:
        print ("Case #" + str(i+1) + ": " + "IMPOSSIBLE")
