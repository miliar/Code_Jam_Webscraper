a=open("test.in").readlines()
f=open("ans","w")
t = int(a.pop(0))
for case_no in range(1,t+1):
    i1,i2=int(a.pop(0)),int(a.pop(4))
    
    a1=[i.split(' ') for i in a[:4]]
    a2=[i.split(' ') for i in a[4:]]
    
    def card_map(x):
        n=[]
        for i in x:
            for j in i:
                n.append(int(j))
        return n
        
    a1=card_map(a1)
    a2=card_map(a2)
    
    def get_row(r,x):
        return set(r[(x-1)*4:x*4])
    
    b1=get_row(a1,i1)
    b2=get_row(a2,i2)
    ans=set.intersection(b1,b2)
    
    f.write("Case #%d: "%case_no)
    if len(ans)==1:
        f.write(str(ans.pop()))
    elif len(ans) > 1:
        f.write("Bad magician!")
    else:
        f.write("Volunteer cheated!")
    f.write("\n")
    a=a[8:]
f.close()
