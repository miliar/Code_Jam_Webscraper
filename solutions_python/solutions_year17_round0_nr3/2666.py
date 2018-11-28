def ls(s,j):
    for l in range(j-1,-1,-1):
        if s[l]==1:
            return j-l-1
        
def rs(s,j):
    for l in range(j+1, len(s)):
        if s[l]==1:
            return l-j-1
            
content=[]
output=[]
with open("C-small-1-attempt0.in") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content.pop(0)
for NK in content :
    input1=NK.split()
    flag=0
    
    n=input1[0]
    k=input1[1]
    if int(n)==int(k):
        output.append([0,0])
       # print n,k,0,0
        continue
        
    arr=[]
    a=[]
    arr.append(1)
    for i in range(1,int(n)+1):
        arr.append(0)
    arr.append(1)

#for i in range(0,int(n)+2):
#    print arr[i]
    maxmin=0
    for inc in range(int(k)):
        #print "yo"
        maxmin=0
        flag=1
        for i in range(1,int(n)+1):
        
            if arr[i]==1:
                #print "cont"
                continue
            if maxmin<min(ls(arr,i),rs(arr,i)):
               # print "min change"
                maxmin=min(ls(arr,i),rs(arr,i))
                flag=i
                
            elif min(ls(arr,i),rs(arr,i))==maxmin:
                #print "max check"
                if max(ls(arr,i),rs(arr,i))>max(ls(arr,flag),rs(arr,flag)):
                    #print "max change"
    
                    flag=i               
                
                            
        arr[flag]=1
    #for i in range(0,int(n)+2):
        #print arr[i]
    ans1=[]
    ans1.append (max(ls(arr,flag),rs(arr,flag)))
    ans1.append (min(ls(arr,flag),rs(arr,flag)))
    #print n,k,ans1
    output.append(ans1)
num0=1
fo = open("BS_ans1.in","wb")
for j in output :
	j_1= "Case #" + str(num0) + ": " + str(j[0]) + " " + str(j[1])  
	print j_1
	fo.write(j_1+"\n")
	num0+=1
fo.close()
#print min(ls(arr,flag),rs(arr,flag))

#print ls(arr,3)
#print rs(arr,3)
#print arr[1]
#print arr.find(
