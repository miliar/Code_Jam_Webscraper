T = int(raw_input())

def invoke(s):
	for j in range(c):
		if (c_arr[j][:2] == s[-2:]) or (c_arr[j][:2] == s[-2:][::-1]) :
			s = s[:-2] + c_arr[j][2]
			return s
	for k in range(0,len(s)-1):
		for j in range(d):
			if (d_arr[j] == s[-1] + s[k]) or (d_arr[j] == s[k] + s[-1]):
				return ""		
	return s

for t in range(T):
	arr = raw_input().split(" ")
	c = int(arr[0])
	c_arr = arr[1:c+1]
	d = int(arr[c+1])
	d_arr = arr[c+2:c+d+2]
	s = arr[-1]
	s1 = ""
	for i in s:
		s1 += i
		s1 = invoke(s1)

	print "Case #%d: %s" % (t+1,"[" + ", ".join(s1) + "]")
	
