ss=open("c:/Users/shivnamha/Desktop/A-large.in","r+")
sf=open("c:/Users/shivnamha/Desktop/1st.out","r+")
a=ss.readline()
x=1
def __str__():
     if(((k+1)%pow(2,n))==0):
         return("Case #%d: %s"%(x,'ON'))
     else:
         return("Case #%d: %s"%(x,'OFF'))
for i in ss:
    n,k=i.split(' ')
    n=int(n)
    k=int(k)
    s=__str__()
    sf.write(s)
    sf.write('\n')
    x=x+1
    
