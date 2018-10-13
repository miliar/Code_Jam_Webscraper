f= open("lol2.in","r")
f2=open("out.out","w")
dat = f.read().splitlines()
data = dat[1:]
print data

def digitsum(x):  
    total=0  
    for number in str(x):  
        total+=int(number) 
    
    return total 
invite=0
result=""
counter=1
for test_case in data:
    print counter, test_case
    temp=test_case.split(" ")
    smax=int(temp[0])
    s=temp[1]
    for i in range(smax+1):
        #print "sum :", digitsum(test_case[2:i+2]), "ind: ",i
        if  i > (digitsum(test_case[2:i+2])+invite):
            invite+=1
    result+="Case #"+str(counter)+": "+str(invite)+"\n"
    invite=0
    counter+=1
f2.write(result)
f2.close()