def f(n):	
	n = str(n)
	i = 1
	if len(n) == 1: return int(n)
	while True:
		if n[i] < n[i-1]:
			n = str(int(n[:i+1])-1) + (len(n)-i-1)*"9"
			i = 0
		if i == len(n)-1: break
		i += 1
	return int(n)
	
x = int(input())
l = []

for i in range(x):
    l.append(int(input()))
for i in range(x):
	print("Case #%d: %d" %(i+1, f(l[i])))