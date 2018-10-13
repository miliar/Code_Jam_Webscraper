def check(order):
    for x in xrange(len(order) - 1):
        if order[x] > order [x+1]:
            return False
    return True
x=0
count=1
outp=open("Output.txt","a")
with open("B-small-attempt1.in","r") as inpu:
    for line in inpu:
        line=line.strip("\n")
        inp= line.split(" ")
        if x==0:
            x+=1
            continue
        flag=True
        while(flag):
            order = list(str(line))
            if(check(order)):
                outwr="Case #"+str(count)+": "+str(line)
                count+=1
                print outwr
                outp.write(outwr)
                outp.write("\n")
                flag=False                    
            else:
                line=long(line)-1
                
            

outp.close()    
