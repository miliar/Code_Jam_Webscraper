import sys
f=open('saas.txt','w')
n = int(input())
for m in range (n):
    s = sys.stdin.readline()
    s = s.split()
    k = int(s[1])
    s = s[0]
    s = list(s)
    p = 0
    for i in range (len(s)-k+1):
        if s[i] == '-':
            p +=1
            s[i]= '+'
            for j in range (1,k):
                if s[i+j] == '-':
                    s[i+j]= '+'
                elif s[i+j] == '+':
                    s[i+j] = '-'
        if s[i] == '+':
            pass
    if len(set(s))==1:
        pio = 'Case '+'#'
        pio = pio+str(m+1)+':'
        p = pio+' '+str(p)+'\n'
        f.writelines(p)
    else:
        pio = 'Case ' + '#'
        pio = pio + str(m+1) + ':'+' '+'IMPOSSIBLE'+'\n'
        f.writelines(pio)
