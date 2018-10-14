num = int(raw_input())
cont=1

while(cont<=num):
	s, k = raw_input().split()

	n = len(s)
	k = int(k)
	s = list(s)

	res = 0

	for i in range(n - k + 1):
	    if s[i] == "-":
	        res += 1
	        for j in range(k):
	            if s[i + j] == "+":
	                s[i + j] = "-"
	            else:
	                s[i + j] = "+"

	if "-" in s:
		print "Case #{}: IMPOSSIBLE".format(cont)
	else:
		print "Case #{}: {}".format(cont, res)

	cont+=1
