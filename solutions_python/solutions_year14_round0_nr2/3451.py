f = open('B-small-attempt1.in', 'r')
out=open('out.txt', 'w')
cases=f.readline()
x=0
while x<cases:
        time= []
        line = f.readline()
        if not line: break
        c=line.split()
        result=0.0
        old=float(c[2])/2.0

        for i in range(0,5000):
                time.append(float(c[0])/(2+i*float(c[1])))
                result =sum(time)

                if(float(result+float(c[2])/(2+i*float(c[1])+float(c[1]))) < float(old)):
                        old=float(result+float(c[2])/(2+i*float(c[1])+float(c[1])))
        out.write("Case #"+str(x+1)+": "+str(old)+"\n")
                
                        
                        
               
               
        x+=1
out.close()
