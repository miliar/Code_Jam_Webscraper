N = int(input())

for i in range(N):
    s_in = input().split()
    s = s_in[0]
    s_len = int(s_in[1])
    count = 0
    for j in range(1,len(s)-s_len+2):
        if (s[j-1]=='-'):
            count += 1
#
            for k in range(s_len):
                if (s[j-1+k]=='-'):
                    #s[j].replace('-','+')
                    s = s[0:j-1+k] + '+' + s[j+k:len(s)]
                elif (s[j-1+k]=='+'):
                    #s[j].replace('+','-')
                    s = s[0:j-1+k] + '-' + s[j+k:len(s)]
#
#            if (s[j-1]=='-'):
#                #s[j].replace('-','+')
#                s = s[0:j-1] + '+' + s[j:len(s)]
#            elif (s[j-1]=='+'):
#                #s[j].replace('+','-')
#                s = s[0:j-1] + '-' + s[j:len(s)]
#            if (s[j]=='-'):
#                #s[j+1].replace('-','+')
#                s = s[0:j] + '+' + s[j+1:len(s)]
#            elif (s[j]=='+'):
#                #s[j+1].replace('+','-')
#                s = s[0:j] + '-' + s[j+1:len(s)]
#            if (s[j+1]=='-'):
#                #s[j+2].replace('-','+')
#                s = s[0:j+1] + '+' + s[j+2:len(s)]
#            elif (s[j+1]=='+'):
#                #s[j+2].replace('+','-')
#                s = s[0:j+1] + '-' + s[j+2:len(s)]

    if ('-' in s):
        ret = 'IMPOSSIBLE'
    else:
        ret = str(count)
    print ('Case #'+str(i+1)+': '+ret)
