filename='C:\\Users\\Brijesh\\Desktop\\Python\\input.in'
output_file = 'C:\\Users\\Brijesh\\Desktop\\Python\\output.txt'
fo = open(output_file,'w');
f=open(filename,'r')
file =f.readlines()
tc = int(file[0])
line = 1


for test in range(1,tc+1):
    print(test)
    temp= file[line].split()
   # print temp
    a = int(temp[0])
    b = int(temp[1])
    k = int(temp[2])
    line+=1
    
    min = 0
    for i in range(a):
        for j in range(b):
            if i&j < k:
                min+=1 
    print min            
    res= "Case #"+str(test)+": "+str(min) 
               
    fo.write(res)                    
    fo.write('\n')
                                                        
f.close()    
fo.close()            
