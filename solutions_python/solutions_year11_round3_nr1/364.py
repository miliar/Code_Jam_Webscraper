def print_matrix(m):
	for line in m:
		print line
		
def solve(r,c,arr):
	for i in range(r):
		for j in range(c):
			if arr[i][j]=='#':
				if j+1<c and i+1<r and arr[i][j+1]=='#' and arr[i+1][j]=='#' and arr[i+1][j+1]=='#':
					arr[i][j]='/' 
					arr[i][j+1]='\\' 
					arr[i+1][j]='\\' 
					arr[i+1][j+1]='/'
				else:
					return ['Impossible']

	return arr
	
#main
from time import time
if __name__ == "__main__":
	def getInts():
		return map(int, input.readline().rstrip('\n').split(' '))
	start_time=time()
	output = open('C:/Users/Jenny/Desktop/gcj/output', 'w')
	input = open("C:/Users/Jenny/Desktop/gcj/in.txt", "r")
	T = int(input.readline())
	for case in range(1, T + 1):
		r=getInts()
		p=[]
		for line in range(r[0]):
			p.append(list(input.readline().rstrip('\n')))
		ans = solve(r[0],r[1],p)
		s = "Case #%d:\n" %(case)
		if len(ans)==1 and ans[0]=='Impossible':
			s = s+'Impossible\n'
		else:
			for i in range(len(ans)):
				for j in range(len(ans[i])):
					s=s+ans[i][j]
				s=s+"\n"
		print s,
		output.write(s)
	print "Total time: %d msec"%(1000*(time()-start_time))