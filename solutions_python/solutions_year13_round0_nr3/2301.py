import gmpy
f=open("E:\q.txt")
q=f.readlines()
for i in range(1,int(q[0].rstrip())+1):
    q[i]=q[i].rstrip()
    a,b=q[i].split()
    cnt=0
    for k in range(int(a),int(b)+1):
         if gmpy.is_square(k) and k<10:
             cnt=cnt+1
         z = str(k) 
         l=len(z)/2
         if z[:l]==z[-l:][::-1]:
             if gmpy.is_square(k):
                 temp=gmpy.sqrt(k)
                 a=str(temp)
                 m=len(a)/2
                 if a[:l]==a[-m:][::-1]:
                     cnt=cnt+1
    print "Case #"+str(i)+':'+str(cnt)
