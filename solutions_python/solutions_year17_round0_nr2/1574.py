inp =  open("B.in", "r")
T = int(inp.readline())
cases = []
for line in inp:
	cases.append(int(line))
inp.close()

def is_valid(x):
	data = [int(i) for i in str(x)]
	for i in range(1, len(data)):
		if data[i] < data[i-1]:
			return False
	return True

	
out =  open("B.out", "wb") 


for cs in range(T):
	x = cases[cs]
	while x >= 0:
		if is_valid(x):
			out.write("Case #%d: %d\n" % ( cs+1, x))
			break
		x -= 1

out.close()