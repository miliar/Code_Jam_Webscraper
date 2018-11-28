import sys

def solution():
	testcase = int(sys.stdin.readline().strip())
	case =1
	for tc in range(testcase):
		a,b = map(int,sys.stdin.readline().strip().split(" "))
		rs =0
		l=dict()
		for n in range(a,b+1):
			arr= str(n)
			for i in range(1,len(arr)):
				t = arr[i:] + arr[0:i]
				#print n,t
				m = int(t)
				if m > n and m<=b and m>=a and l.get(arr+"_"+t)==None and l.get(t+"_"+arr)==None: 
					#print "VO"
					rs =rs+1  
					l[arr+"_"+t] = 1
		print "Case #%d: %d"%(case,rs)
		case+=1
solution()
