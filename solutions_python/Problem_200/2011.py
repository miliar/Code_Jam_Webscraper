n=int(input())
for x in range(n):
    m=list(input())
    for y in range(len(m)-1,0,-1):
        if int(m[y])<int(m[y-1]):
            l=len(m[y:])
            del m[y:]
            m.extend(list('9'*l))
            m[y-1]=str(int(m[y-1])-1)
    if m[0]=='0':
        del m[0]
    print(r'Case #'+str(x+1)+': '+''.join(m))
