def pancake(a):
    pancake=list(a.split()[0])
    k=int(a.split()[1])
    #pancake,flips
    count=0
    for i in range(len(pancake)-k+1):
        if pancake[i]=='-':
            for j in range(i, i+k):
                if pancake[j]=='-':
                    pancake[j]='+'
                else:
                    pancake[j]='-'
            count=count+1 
    if "-" in pancake:
        return "IMPOSSIBLE"
    else:
        return count
        
f=open('A-large.in', 'r')
all_content=f.readlines()
all_content = [x.strip() for x in all_content] 
T=int(all_content[0])
f = open('Output.txt','w')
for i in range(0, T):
    output=pancake(all_content[i+1])
    #print "Case #{}:".format(i),res,file=f
	#print("Case score for %s is %s  " % (name, score))
    f.write("Case #%s: %s\n" % (i+1, output))
f.close()