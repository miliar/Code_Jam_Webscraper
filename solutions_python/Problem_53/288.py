

def solve(n,k, array):
	if k==0:
		return False
	return array[n]==k%(array[n]+1)

if __name__ == "__main__":
	array = range(0,101)
	for i in range(2,101):
		array[i] = array[i-1]*2+1
	f = open("c:\input.txt", "r")
	num = int(f.readline().strip())
	for i in range(1,num+1):
		(n,k) = f.readline().strip().split(" ")
		temp = solve(int(n),int(k), array)
		if temp:
			print "Case #%d: %s" %(i,"ON")
		else:
			print "Case #%d: %s" %(i,"OFF")