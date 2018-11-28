f = open('C:\Codejam\B-small-attempt1 (1).in', 'r')
f2 = open('C:\Codejam\Outputfile.txt', 'w')

ip = list(f)

temp3 = ip[0].rsplit()
test = int(temp3[0])
z=1

for i in range(test):
    
    #main code for each program begins here
    
        
    temp2 = ip[z].rsplit()
        
    a= int(temp2[0])
    b= int(temp2[1])    
    k= int(temp2[2])    
        
    z+=1
    count = 0
    for l in range(0,a):
        for m in range(0,b):
            t5= l & m
            if t5 < k and t5>=0:
                count +=1
    
    
    s = str("Case #" + str(i+1) + ": " + str(count))
    print s
    f2.write(s)
    f2.write("\n")
f2.close()    