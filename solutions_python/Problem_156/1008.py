import fileinput
import bisect

words = []
for line in fileinput.input():
	for word in line.split():
		words.append(word.strip())
def nextInt():
	return int(words.pop(0))
def nextStr():
	return words.pop(0)


def main():
	T = nextInt()
	for _t in range(T):
		d = nextInt()
		ps = []
		for j in range(d):
			ps.append(nextInt())
		ps.sort()
		print "Case #%d: %d"%(_t+1, go(ps))
			 
def is_sorted(lst):
   	return lst == sorted(lst) 

def ps(x):
	x = x ** 0.5
	return int(x) == x

def go(a):
	n = len(a)
	a2 = a
	case1 = a[-1]

	num_same = sum([1 for i in a if i == a[-1]])
	if a[-1] <= 3 or num_same >= a[-1]/2:
		return case1

	a = a2[:]
	last = a.pop()
	bisect.insort(a, int(last/2) + last%2)
	bisect.insort(a, int(last/2))

	case2 = go(a) + 1

	case3 = 9999999999

	a = a2[:]
	if ps(a[-1]):
		last = a.pop()
		x = int(last ** .5)
		for i in range(x):
			bisect.insort(a, x)
		case3 = go(a) + x - 1


	return min(case1, case2, case3)





main()