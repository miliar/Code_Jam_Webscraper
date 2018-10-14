# n is the array of chars (+ or -)
# k is the number of pancakes that can be flipped at once
def flips(n,k):
	flip = 0
	for (i,s) in enumerate(n):
		if not s:
			for j in range(k):
				if i+j>=len(n):
					return -1
				n[i+j] = not n[i+j]
			flip+=1
	return flip


inf = open("A-large.in","r")
outf = open("output.txt","w+")
num = int(inf.readline())
for c in range(num):
	dat = inf.readline().split()
	n = list(map(lambda n: True if n=='+' else False, dat[0]))
	k = int(dat[1])
	res = flips(n,k)
	if res<0:
		outf.write('Case #%d: IMPOSSIBLE\n'%(c+1))
	else:
		outf.write('Case #%d: %d\n'%(c+1,res))

inf.close()
outf.close()
