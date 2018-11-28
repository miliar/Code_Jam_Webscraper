myinf = "sample.txt"
myinf = "A-large.in"

#myout = open("output.txt",'wt')
myout = open("output1.txt",'wt')
#myout = open("output2.txt",'wt')

myin = open(myinf,'rt').read().split('\n')
num_case = int(myin[0])
print(num_case)
for i in range(num_case):

    shift=i+1
    inputs = myin[shift].split()
    smax=int(inputs[0])
    aud=inputs[1]

    total = 0
    add = 0
    for j in range(smax+1):
        #print(aud[j])
        if(int(aud[j]))==0:
            total-=1
            if(total<0):
                add+=1
                total=0
        else:
            total+=int(aud[j])-1
    
    print(smax, aud,total,add)
    
    myout.write("Case #%d: %s\n"%((i+1),add))

myout.close()    
