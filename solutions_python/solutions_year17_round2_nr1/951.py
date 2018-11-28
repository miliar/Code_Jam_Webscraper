t=int(input())
for i in range(t):
    x,y=input().split(' ')
    x,y=[int(x),int(y)]
    h=[]
    s=[]
    for j in range(y):
        a,b=input().split()
        a,b=[int(a),int(b)]
        h.append(a)
        s.append(b)
    for j in range(len(h)):
        h[j]=(x-h[j])/s[j]
    print('Case #'+str(i+1)+': '+str(x/max(h)))
