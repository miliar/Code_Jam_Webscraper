def is_tidy(n):
	s = str(n)
	for i in range(len(s)-1):
		if s[i]>s[i+1]:
			return False
	return True

t = int(input())
for index in range(t):
	s = list("0"+input())
	for i in range(len(s)-2,-1,-1):
		if int(s[i]) > int(s[i+1]):
			s[i+1] = "9"
			j = i
			while s[j] == "0":
				s[j] = "9"
				j-=1
			s[j] = str(int(s[j]) - 1)
	for i in range(len(s)-1):
		if int(s[i]) > int(s[i+1]):
			s[i+1] = s[i]
	print("Case #"+str(index+1)+": "+str(int("".join(s))))
