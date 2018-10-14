import sys

res = 0
largest_final = 0

def divide(k):
	if k%2 == 0:
		return k/2, k/2
	return k/2 + 1, k/2

def dfs(p, iteration):
	global res, largest_final

	# Checking code
	p = sorted(p)
	np = [x+iteration for x in p]
	largest_final = min(largest_final, np[-1])
	# print p,np, iteration
	if iteration > 100 or p[-1] == 1:
		res = largest_final
		return

	iteration += 1
	largest_diner = p[-1]
	if largest_diner != 9:
		(a,b) = divide(largest_diner)
		p[-1] = a
		p.append(b)
		dfs(p, iteration)
	else:
		tp = list(p)
		tp[-1] = 6
		tp.append(3)
		dfs(tp, iteration)

		tp2 = list(p)
		tp2[-1] = 5
		tp2.append(4)
		# print "TP2", tp2, p
		dfs(tp2, iteration)

fin = open("B-small-attempt4.in","r")
# fin = open("sub-5.in","r")
# fin = open("test2.in2","r")
t = fin.readline().rstrip()
# print t
for i in range(0,int(t)):
	res = 0
	buf = fin.readline()
	p = fin.readline().rstrip().split(' ')
	p = [int(x) for x in p]
	p = sorted(p)
	largest_final = p[-1]
	dfs(p, 0)
	print "Case #" + str(i+1) + ": " + str(res)


