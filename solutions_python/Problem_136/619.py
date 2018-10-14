def time (farm,addcoo,tar):
    
    hv_coo=2
    time=0.0
    while 1:
        time1=tar/hv_coo
        time2=farm/hv_coo
        time3=tar/(hv_coo+addcoo)
       
        if (time+time1) < (time+time2+time3):
            time=time+time1
            
            break
        else:
            
            time=time+time2
            hv_coo=hv_coo+addcoo
            

      
    return str(time)    


file=open("c:/users/rhv/Desktop/code_jam/2014/B-large.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/2014/cookie_farm.py2014_sample_out.txt","w")
m=file.readline()
i=0
l = m.split()


while i<int(l[0]):
    k=[]
    m1=file.readline()
    m2=m1.split()
   
   
    j=0
    while j<3:
        temp=float(m2[j])
        k.append(temp)
        j=j+1
      
    ans = time(k[0],k[1],k[2])
    
    d = "Case #" + str(i+1) +": "+ans+"\n"
    file1.write(d)
    i=i+1

file.close()
file1.close()
