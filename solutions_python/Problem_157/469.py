# terrible naive hacky solution

t = {
'11':('1',0),
'1i':('i',0),
'1j':('j',0),
'1k':('k',0),

'i1':('i',0),
'ii':('1',1),
'ij':('k',0),
'ik':('j',1),

'j1':('j',0),
'ji':('k',1),
'jj':('1',1),
'jk':('i',0),

'k1':('k',0),
'ki':('j',0),
'kj':('i',1),
'kk':('1',1)
}

def mult(a,b):
    ret = t[a[0] + b[0]]
    #print("test",ret,a[0] + b[0])
    ret2 = [ret[0],ret[1]]    
    ret2[1] ^= a[1] ^ b[1]
    #print(a,b,ret2)
    return ret2

s = open("in")
n2 = int(s.readline().strip())

o = open("out","w")
for i in range(1,n2+1):
    print(i)
    l,x = [int(j) for j in s.readline().strip().split()]
    y = s.readline().strip()

    #print(y,x)
    a = [y[0],0]
    if x%4 == 0:
        #print("parity")
        o.write("Case #"+str(i)+": NO\n")
        continue

    for j in range(1,len(y)):
        a = mult(a,[y[j],0])
    b = ['1',0]
    for j in range(x%4):
        b = mult(b,a)
    if b != ['1',1]:
        #print("total")
        o.write("Case #"+str(i)+": NO\n")
        continue
    #print("passed init")
    a = ['1',0]
    found = False
    for j in range(min(l*x-2,l*4+1)):
        a = mult(a,[y[j%l],0])
        #print(j,a)
        if a == ['i',0]:
            b = ['1',0]
            for k in range(j+1,min(l*x-1,j+2+l*4)):
                b = mult(b,[y[k%l],0])
                #print(j,k,y[k%l],b)
                if b == ['j',0]:
                    found = True
                    break
            if found:
                break
    if found:
        o.write("Case #"+str(i)+": YES\n")
    else:
        o.write("Case #"+str(i)+": NO\n")
