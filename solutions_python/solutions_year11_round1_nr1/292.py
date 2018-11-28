myfile=open("A-small-attempt4.in", "r")
inp=myfile.read().split("\n")

fullanswer=""
i=0
for casenumber in range(int(inp[0])):
    i+=1
    var=inp[i].split(" ")
    pd,pg=int(var[1])/100.,int(var[2])/100.

    for d in range(0,int(var[0])+1):
        if pg==1 and pd!=1:
            answer="Broken"
        elif pg==1 and pd==1:
            answer="Possible"
            break
        elif pd>0 and pg==0:
            answer="Broken"
        elif pd==0:
            answer="Possible"
            break
        elif pd==1 and pg==0:
            answer="Broken"
        elif d!=0 and d/float(pd)==int(d/pd) and pg<1:
            if int(d/pd)<=int(var[0]):
                answer="Possible"
                break
            else:
                answer="Broken"
        else:
            answer="Broken"
            
    
    
    fullanswer+="Case #%d: %s\n" % (casenumber+1,answer)



results=open("A.out","w")
results.write(fullanswer)
myfile.close()
results.close()
