N = int(input())

for i in range(N):
    s = input()
    if len(s)==1:
        ret = s
    else:
        j1 = len(s)-2
        j2 = len(s)-1
        while(j1>=0):
            s1 = s[j1]
            s2 = s[j2]
            #print(s1,s2)
            if int(s1)>0:
                if int(s1)>int(s2):
                    s = s[0:j1] + str(int(s1)-1) + s[j1+1:len(s)]
                    #s = s[0:j2] + '9' + s[j2+1:len(s)]
                    s = s[0:j2] + '9'*(len(s)-j2)
            else:
                #s = s[0:j2] + '9' + s[j2+1:len(s)]
                s = s[0:j2] + '9'*(len(s)-j2)

            j1 -= 1
            j2 -= 1
        if s[0]=='0':
            s = s[1:len(s)]
        ret = s

    print('Case #'+str(i+1)+': '+ret)
