

def palier(s,i):
	if i == len(s)-1:
		return False
	if int(s[i+1]) > int(s[i]):
		return False
	elif int(s[i+1]) < int(s[i]):
		return True
	else:
		return palier(s,i+1)


def tidy(s):

	t = ''

	for i in range(len(s)):
		if palier(s,i):
			t += str(int(s[i])-1)
			break
		else:
			t += s[i]

	if len(t) < len(s):
		t += '9'*(len(s)-len(t))
	return t.lstrip('0')

N = int(input())

for i in range(N):
	s = input()
	print('CASE #'+str(i+1)+': '+str(tidy(s)))
