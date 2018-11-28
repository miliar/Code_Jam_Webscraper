import sys

great_sum=-1
index=30
def convertBinary(num):
	global index
	squrs=[]
	for i in range(index):
		squrs.append(pow(2,i))
	sqrs=sorted(squrs,reverse=True)
	binary=[]
	for item in sqrs:
		if num>=item:
			binary.append(1)
			num=num-item
		else:
			binary.append(0)
	return binary

def convertDecimal(b_sum):
	num=0
	for i in range(index):
		if(b_sum[index-i-1]==1):
			num+=pow(2,i)
	return num
			
		
def isEqual(patrik,sam):
	#print "patrik",patrik
	#print "sam",sam
	global great_sum
	cnt=0
	global index
	b_sum=[]
	for i in range(index):
		b_sum.append(0)
	while cnt<len(sam):
		b1=convertBinary(sam[cnt])
		for i in range(index):
			if b1[index-1-i]==1 and b_sum[index-1-i]==1:
				b_sum[index-1-i]=0
			else:
				b_sum[index-1-i]+=b1[index-1-i]
		
		cnt+=1
	sum_sam=convertDecimal(b_sum)

	cnt=0
	sum_patrik=0
	sum_sam_real=0
	while (cnt<len(patrik)):
		sum_patrik+=patrik[cnt]
		cnt+=1
	cnt=0
	while (cnt<len(sam)):
		sum_sam_real+=sam[cnt]
		cnt+=1
	#print sum_sam,sum_patrik,sum_sam_real

	if sum_sam==sum_patrik:
		if sum_sam_real>great_sum:
			great_sum=sum_sam_real
	


	

def cry(cases):
	list_items=[]
	for item in cases:
		list_items.append(int(item))
	print list_items
	temp_list=list_items
	cnt=0
	nos=0
	while cnt<len(temp_list)/2:
		start1=0
		end1=cnt
		start2=end1+1
		end2=len(list_items)
		list_items=temp_list
		
		idx=0
		#print "cnt=",cnt
		while idx<=cnt:
			#print"idx=",idx
			pos=0
			list_items=temp_list
			#print "list",list_items
			for j in range(1,len(list_items)+1) :		
				#print 
				temp=list_items[idx]
				list_items[idx]=list_items[pos]
				list_items[pos]=temp
				pos+=1
				patrik=[]
				sam=[]
				#print pos
				for i in range(start1,end1+1):
					sam.append(list_items[i])
				for i in range(start2,end2):
					patrik.append(list_items[i])
				isEqual(sam,patrik)
				nos+=1
		  	idx+=1
		cnt+=1
	print "nos=",nos
	#sys.exit(0)
		
		
				
		
			
def main():
	print "hello"
	global great_sum
	filename=sys.argv[1]
	fin=open(filename,"r")
	o=open("out.txt","w")
	k=0;
	for line in fin:
		if(k>0):
			if k%2==0:
				cases=line.split()	
				great_sum=-1	
				cry(cases)	
				if great_sum==-1:						
					print>>o, "Case #"+str(k/2)+":","NO"
				else:
					print>>o, "Case #"+str(k/2)+":",str(great_sum)
		k+=1;

if __name__=="__main__":
	main()
