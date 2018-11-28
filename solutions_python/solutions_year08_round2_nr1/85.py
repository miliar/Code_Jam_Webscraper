

def ifGoodTriangle(v1,v2,v3):
	if (v1[0]+v2[0]+v3[0]) % 3 ==0:
		if (v1[1]+v2[1]+v3[1]) % 3 ==0:
			return True
	else:
		return False


def traverse(trees):
	n=len(trees)
	count=0
	for i in range(n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if ifGoodTriangle(trees[i],trees[j],trees[k]):
					count+=1
	return count	

def getTrees(n, A, B, C, D, x0, y0,M):
	trees=[]
	X = x0
	Y = y0
	trees.append([X,Y])
	for i in range(n-1):
		X = (A * X + B) % M
  		Y = (C * Y + D) % M
  		trees.append([X,Y])
	return trees

def main_solve():
	import sys
	
	#sys.stdout=open("debug.output","w")
	
	input_f=open(sys.argv[1],"r")
	first_line=input_f.readline()
	case_num=int(first_line)
	result_f=open("result.output","w")
	
	for i in range(case_num):
		print "do case #%d"%(i+1)
		
		
		parts=input_f.readline().split()
		n=int(parts[0])
		A=int(parts[1])
		B=int(parts[2])
		C=int(parts[3])
		D=int(parts[4])
		x0=int(parts[5])
		y0=int(parts[6])
		M=int(parts[7])
		
		trees=getTrees(n, A, B, C, D, x0, y0,M)
		count=traverse(trees)
		
		result_f.write("Case #%d: "%(i+1))
		result_f.write("%d\n"%count)
		i+=1
	
	
	    
	
	
main_solve()