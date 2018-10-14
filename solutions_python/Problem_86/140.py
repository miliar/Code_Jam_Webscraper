myfile=open("test3.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):
    i+=1
    
    
    fullanswer+="Case #%d: %s\n" % (casenumber+1,"s")



results=open("A.out","w")
results.write(fullanswer)
myfile.close()
results.close()
