n = input()
s = ""
for j in range(n):
    s = raw_input()
    temp = len(s)
    for i in range(len(s)-1 , 0 , -1):
        if ord(s[i]) < ord(s[i-1] ):
            temp = i-1
            s = s[:i-1] + chr(ord(s[i-1])-1) + s[i:]
    res = ""
    if temp == 0 and s[temp] == '0':
        res = '9'*(len(s)-1)
    else:
        res = s[:temp+1] + '9'*(len(s)-temp-1)

    print "Case #" + str(j+1) + ": " + res
    
