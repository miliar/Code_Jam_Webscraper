def perfect(f):
	for i in range(len(f) - 1):
		if int(f[i])>int(f[i+1]):
			return False
	return True

def change(f):
	for i in range(len(f)-1):
		if int(f[i]) > int(f[i+1]):
			f[i] = str(int(f[i])-1)
			f = f[:i+1]+['9' for u in range(len(f)-i-1)]
			return f

for case in range(1,1+int(input())):
	s = input()
	print("Case #%s: " % case,end="")
	t = [str(d) for d in s]
	while not perfect(t):
		t = change(t)
	print((''.join(t)).lstrip('0'))
