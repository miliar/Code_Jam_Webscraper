



		
def getsmallest(v1,v2,n):
	v1.sort()
	v2.sort()
	sum=0
	for i in range(n):
		sum+=v1[i]*v2[-(i+1)]
	return sum
	

def main_solve():
	import sys
	
	#sys.stdout=open("debug.output","w")
	
	input_f=open(sys.argv[1],"r")
	first_line=input_f.readline()
	case_num=int(first_line)
	result_f=open("result.output","w")
	
	for i in range(case_num):
		print "do case %d"%(i+1)
		
		n=int(input_f.readline())
		v1_line=input_f.readline()
		parts=v1_line.split()
		v1=[]
		for part in parts:
			v1.append(int(part))
			
		v2_line=input_f.readline()
		parts=v2_line.split()
		v2=[]
		for part in parts:
			v2.append(int(part))
		
		
		s=getsmallest(v1,v2,n)
		result_f.write("Case #%d: "%(i+1))
		result_f.write("%d\n"%s)
		i+=1
	
	
	    
	
	
main_solve()