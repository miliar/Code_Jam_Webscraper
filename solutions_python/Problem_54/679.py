ss=open("c:/Users/shivnamha/Desktop/B-small-attempt6.in","r+")
sf=open("c:/Users/shivnamha/Desktop/2st.out","w+")
a=ss.readline()
def gcd(x,y):
     g = y
     while x > 0:
         g = x
         x = y % x
         y = g
     return g
x=[]
c=1
def __str__():
     return ("Case #%d: %s"%(c,str((y-(int(x[1])%y))%t)))
for i in ss:
    x=i.split(' ')
    y= (abs(int(x[2])-int(x[1])))
    for j in range(3,int(x[0])+1):
        xx=(abs(int(x[j])-int(x[1])))
        y=gcd(y,xx)
    t=y
    xy=__str__()
   
    sf.write(xy)
    sf.write("\n")
    c=c+1
        
        
                           
                   
    
