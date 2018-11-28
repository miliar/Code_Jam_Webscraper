import sys

total = int(sys.stdin.readline())

def flip(sign):
	if sign == '+':
		return '-'
	else:
		return '+'

def process(p,k):
	l = len(p)
	if l == k:
		allplus = True
		allminus = True
		for i in range(l):
			if p[i]=='-':
				allplus = False
			else:
				allminus = False
		if allplus:
			return 0
		if allminus:
			return 1
		else:
			return -1
	i = 0
	while i<l and p[i]=='+':
		i=i+1
	if i == l:
		return 0
	elif i+k>l:
		return -1
	else:
		for j in range(i,i+k):
			p[j] = flip(p[j])
		recans = process(p[i:],k)
		if recans == -1:
			return -1
		else:
			return recans+1

for i in range (1,total+1):
	params = sys.stdin.readline().split()
	p = list(params[0])
	k = int(params[1])
	ans = process(p,k)
	if ans==-1:
		print("Case #%s:"%i,"IMPOSSIBLE")
	else:
		print("Case #%s:"%i,ans)

