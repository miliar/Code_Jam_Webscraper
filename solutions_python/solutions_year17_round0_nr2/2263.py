#Problem B
 
def isTidy(N):
	return str(N) == ''.join(sorted(str(N)))

def decrement(N):
	string = list(str(N))
	for i in range(len(string)-1, 0, -1):
		if string[i-1] > string[i]:
			N -= 10**(len(string) - i)
			string = list(str(N).zfill(len(string)))
			for j in range(i, len(string)):
				string[j] = '9'
			N = int(''.join(string))
	return N
			
			
		
	
def solve(N):
	if isTidy(N):
		return N
	while not(isTidy(N)):
		N = decrement(N)
	return N

def main():
	f = open("B-large.IN", "r")

	numCases = int(f.readline())

	for i in range(numCases):
		#parse line
		line = f.readline().split(' ')
		N = int(line[0])
		
		#solve
		#print result
		print("Case #", i+1, ": ", solve(N), sep='')
		
		
main()