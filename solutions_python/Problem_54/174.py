def gcd(x,y):
    while True:
        if y==0:
            return x 
        temp=x%y
        x=y
        y=temp


f = open("input.txt", "r")
f2 = open("output.txt","w")
lines = f.readlines()
k =0 
for line in lines:
    a=line.split()
    if  len(a) == 1:
        continue
    k = k+ 1
    b =[]
    for i in range(1,len(a)):
        b.append(int(a[i]))
    b.sort()
#print b
    temp = b[1]-b[0]
    for i in range(0,len(b)-2):
        temp = gcd(temp,b[i+2]-b[i+1])
#print temp
    result = temp-b[0]%temp 
    if result == temp :
        result = 0 
    f2.write( "Case #%d: %d\n"%(k,result))
#    print "Case #%d: %d"%(k,result)
