import numpy as np
file = open('C:\\Users\\V\\Downloads\\filefile.txt','r')
b = file.read()
file.close()    
data = b.split('\n')
n = int(data[0])
file = open('C:\\Users\\V\\Downloads\\Codejam.txt','w')
for i in range(n):
    dat = data[i + 1].split(" ")
    s = (dat[0])
    s = list(s)
    k = int(dat[1])
    ans = 0
    c = 0
    flag = True
    flag2 = True
    while c < len(s):
        if not flag2:
            break
        if s[c] == '-':
            ans += 1
            for u in range(k):
                if c + u < len(s):
                    if s[c + u] == '-':
                        s[c + u] = '+'
                    else:
                        s[c + u] = '-'
                else:
                    flag = False
                    flag2 = False
                    file.write("Case #" + str((i + 1)) + ": "  + "IMPOSSIBLE" + '\n')
                    #print "Case #" + str((i + 1)) + ": "  + "IMPOSSIBLE"
                    break
            # print str(s)
        c += 1
    if flag:
        for o in s:
            if o == '-':
                flag2 = False
                file.write("Case #" + str((i + 1)) + ": "  + "IMPOSSIBLE" + '\n')
                #print "Case #" + str((i + 1)) + ": "  + "IMPOSSIBLE"
                break
    if flag2:
        file.write("Case #" + str((i + 1)) + ": "  + str(ans) + '\n')
        #print "Case #" + str((i + 1)) + ": "  + str(ans)
file.close()