from math import sqrt
file=open("small.in","r")
file.readline()
l=[]
case=1
text=open("output.txt","a")
for line in file:
    line=line.rstrip("\n").split()
    l.append(line)
file.close()
for interval in l:
    count=0
    for num in range(int(interval[0]),int(interval[1])+1):
        s=str(num)
        if s in "1,4,9":
            count+=1
        else:
            for n in range(0,len(s)/2):
                if s[n]==s[-n-1]:
                    if n==len(s)/2-1:
                        s=str(sqrt(num)).split(".")
                        if s[1]=="0":
                            root=s[0]
                            for m in range(0,len(root)/2):
                                if root[m]==root[-m-1]:
                                    if m==len(root)/2-1:
                                        count+=1
    text.write("Case #%d: %d\n" % (case,count))
    case+=1
text.close()
                    
        
            
                    
