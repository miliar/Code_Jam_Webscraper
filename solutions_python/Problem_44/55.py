import math
def get_t(points):
    sumx=0
    sumvx=0
    sumy=0
    sumvy=0
    sumz=0
    sumvz=0
    for i in xrange(1,len(points)+1):
        point=points[i]
        sumx+=point[0]
        sumvx+=point[3]
        sumy+=point[1]
        sumvy+=point[4]
        sumz+=point[2]
        sumvz+=point[5]
    up=-sumx*sumvx-sumy*sumvy-sumz*sumvz
    down=sumvx**2+sumvy**2+sumvz**2
                
    if down==0:
        return 0
    else:
        t=up*1.0/down
        if t<0:
            return 0
        else:
            return t

def get_dt(points):
    N=len(points)
    t=get_t(points)
    sumx=0
    sumy=0
    sumz=0
    for i in xrange(1,N+1):
        point=points[i]
        sumx+=point[0]
        sumy+=point[1]
        sumz+=point[2]
    sumx=sumx*1.0/N
    sumy=sumy*1.0/N
    sumz=sumz*1.0/N
    value_0=math.sqrt(sumx**2+sumy**2+sumz**2)
    if t==0:
       return (value_0,0)
    else:
        sumxx=0
        sumyy=0
        sumzz=0
        for i in xrange(1,N+1):
            point=points[i]
            sumxx+=point[0]+t*point[3]
            sumyy+=point[1]+t*point[4]
            sumzz+=point[2]+t*point[5]
        sumxx=sumxx*1.0/N
        sumyy=sumyy*1.0/N
        sumzz=sumzz*1.0/N
        value_1=math.sqrt(sumxx**2+sumyy**2+sumzz**2)
        if value_0<value_1:
            return (value_0,0)
        else:
            return (value_1,t)

def main():
    f=open('Blarge.in','r')
    outfile = open("test2.out", 'w')
    lines=f.readlines()
    T=int(lines[0])
    i=1
    count=1
    while count<=T:
        N=int(lines[i])
        i+=1
        points={}
        for k in xrange(i,i+N):
            a=lines[k][:-1]
            points[k-i+1]=[int(j) for j in a.rsplit(" ")]
        (d,t)=get_dt(points)
        print "Case #" +str(count)+": "+str(d) +" "+str(t)
        outfile.write('Case #'+str(count)+': '+str(d) +" "+str(t)+'\n')
        i+=N
        count+=1
    


if __name__ == "__main__":
   main()
          
            

        
    
            
        
            
        
        
        
        
        
