import math

f = open("2in.txt").read().split("\n")
writeF = open("2out.txt","w")

def lengthof(number):
    return int(math.floor(math.log10(float(number)))+1)

def istidy(number,length):
    if length==1:
        return 1
    else:
        for i in range(0,length):
            if int(number/10**(length-i)%10)>int(number/10**(length-i-1)%10):
                #print("%d > %d"%(number/10**(length-i)%10,number/10**(length-i-1)%10))
                return 0
    return 1
    
def getfault(number,length):
    for i in range(0,length+1):
        if number/10**(length-i)%10>number/10**(length-i-1)%10:
            #print ("The fault is %d"%i)
            return i
            
# print(getfault(132,3))
            
def getnumber(number,length):
    if istidy(number,length)==1:
        return number
    else:
        faultdigit=getfault(number,length)-1
        # print(faultdigit)
        temp=number%(10**(length-faultdigit-1))
        nextnumber=number-temp-1
        #print("%d = %d - %d - 1" %(nextnumber,number,temp))
        return getnumber(nextnumber,lengthof(nextnumber))


for i in range(1,(int)(f[0])+1):
    n=f[i]
    # print (n);
    length=lengthof(n)
    writeF.write("Case #"+str(i)+": "+str(getnumber(int(n),length))+"\n")