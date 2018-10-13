def create_list(n):
	lista = []
	for i in range(n):
		l = raw_input().split(" ")
		lista.append(l)
	return lista


def palindrome(n):
	s = str(n)
	new_s = ""
	for i in range(len(s)):
		new_s += s[len(s) - i - 1]

	if(int(new_s) == n):
		return True
	else:
		return False

def square(n):
	a = n**(.5)
	a = int(a)
	if(a**2 == n):
		if(palindrome(a)):
			return True
		else:
			return False
	else:
		return False


def counter(l):
	c = 0
	for i in range(int(l[0]), int(l[1]) + 1):
		if(square(i) and palindrome(i)):
			c += 1
	return c



l = create_list(input())
for i in range(len(l)):	
	print "Case #" + str(i + 1) + ": " + str(counter(l[i]))