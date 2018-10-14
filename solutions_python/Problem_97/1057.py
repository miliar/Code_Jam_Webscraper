

def recycle(num):
 l=len(str(num))
 numlist=list()
 for i in range(1,l):
        new_num=num
        end_digits=new_num%(10**i)
        new_num=new_num/(10**i)
 	len_num=len(str(new_num))
 	end_digits=end_digits*(10**len_num)
 	end_digits=end_digits+new_num
 	numlist.append(end_digits)
 return numlist	

def garbage_can(a,b):
	numtable=list()
	for i in range(a,b+1):
   		result=recycle(i)
   		for j in result:
   		    if (i>=a) and (i<j) and (j<=b)and (i<b):
   		    	if not ((j,i) in numtable or (i,j) in numtable ):
   		    		numtable.append((i,j))
	return numtable



def main():
 inputfile=open("input.txt","r+")
 num=int(inputfile.readline().strip())
 
 for i in range(1,num+1):
   line=inputfile.readline().strip().split()
   
   a=int(line[0])
   b=int(line[1])
   numtable=garbage_can(a,b)
   print "Case #"+str(i)+": "+str(len(numtable))

if __name__=="__main__":
 main()


   
   
