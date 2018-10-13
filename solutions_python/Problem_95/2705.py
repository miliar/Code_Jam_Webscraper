def hell(j):
    o_p=''
    var=b[j+1]
    for i in range(len(var)):
            a=m_p.find(var[i])
            a=a+ord('a')
            if a==123:
                a=32
            if a!=96:
                o_p=o_p+chr(a)    
    return 'Case #'+str(j+1)+': '+o_p
f = open('C:\Documents and Settings\ADMIN\Desktop\jhb.txt', 'r')
but = open('C:\Documents and Settings\ADMIN\Desktop\jhb1.txt', 'r+')
b=f.readlines()
t=int(b[0])
m_p='ynficwlbkuomxsevzpdrjgthaq '
o_p=''
for j in range(t):
     s=hell(j)
     but.write(s)
     but.write('\n')
f.close()
but.close()
