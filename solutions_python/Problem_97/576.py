def rot(l):
	for i in range(len(l)):
		yield l
		l = l[1:] + l[0]

def find(A,B):
	for i in range(A,B+1):
		s = str(i)
		if s[0] == "0": continue
		for t in rot(s):
			if t[0] == "0" or not s < t or int(t) > B: continue
			yield (s,t)

def say(A,B):
	return len(set(find(A,B)))

T = int(input())
for i in range(1, T+1):
	A,B = input().split()
	print("Case #", i, ": ", say(int(A),int(B)), sep="")
