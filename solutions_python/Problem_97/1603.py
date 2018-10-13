f=open('C:/Users/acer/Desktop/CJ/C/C-small-attempt0.in')
bl=f.readlines()
f.close()
n=bl[0]
k=int(n)
i=1
pyes='0'

f=open('C:/Users/acer/Desktop/CJ/C/co.txt','w')
while i <= k :
    count=0
    m= bl[i].split()
    
    start=int(m[0])
    end=int(m[1])
    p=start
    for p in range(start,end+1):
        q=len(m[0])
        for r in range (1,q):
            pair=str(p)[q-r:q]+str(p)[0:q-r]
            if int(pair) > p :
                if int(pair) <= end:
                    if int(pair) != int(pyes):
                        count +=1
                        pyes=pair                     
                                             
                    
                


    
    f.write('Case #'+ str(i) + ': '+(str(count) + '\n'))
    i=i+1
f.close()
        
        
    
    


    
	


