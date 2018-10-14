def check(s):
        flg=False
        for i in range(0,len(s)-1):
                if(s[i]>s[i+1]):
                        flg=True
                        break
                        
        return flg
        

r=open('big.txt','r')
w=open('bigans.txt','w')
t=int(int(r.readline()))
temp=t
while t>0:
        n=int(r.readline())
        if not check(str(n)):
                w.write('Case #'+str(temp-t+1)+': '+str(n)+'\n')
        else:
                i=1
                while check(str(n-n%10**(i)-1)):
                        i=i+1
                #print("Case #{}: {}".format(temp+1-t,n-n%10**(i)-1))  
                w.write('Case #'+str(temp-t+1)+': '+str(n-n%10**(i)-1)+'\n')                           
        t=t-1
