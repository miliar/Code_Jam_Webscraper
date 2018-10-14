import os
import random

def read_input():
	file_name = "%s/small.in" % os.getcwd()
	return open(file_name, "r")

def basecase(Ps):
	if len(Ps) == 0: return True
	for Pi in Ps:
		if Pi > 1: return False
	return True

def get_split(Ps, n):
	t, split = 0, []
	ref = max(Ps)
	for Pi in Ps:
		if Pi == ref:
			t += 1
			split.append(Pi / n)
			split.append(Pi - Pi / n)
		else:
			split.append(Pi)
	return t, split

def time(Ps):
	ref = max(Ps)
	ans = [ref]
	for n in range(2, ref+1):
		if basecase(Ps):
			ans.append(1)
		else:
			t, split = get_split(Ps, n)
			ans.append(min(max(Ps), t+time(split)))
	return min(ans)

def get_ans(Ps, num):
	val = time(Ps)
	return "Case #%d: %d" % (num, val)

def make_output(ans):
	file_name = "%s/small.out" % os.getcwd()
	f = open(file_name, "w")
	f.write(ans)
	f.close()

def main():
	ans = ""
	f = read_input()
	
	T = int(f.readline())
	for i in range(T):
		print i
		D = int(f.readline())
		Ps = [int(x) for x in f.readline().split()]
		ans += get_ans(Ps, i+1)
		if i < T-1: ans += "\n"

	f.close()
	make_output(ans)

main()

print get_ans([3], 1)
print get_ans([1, 2, 1, 2], 1)
print get_ans([4], 1)
print get_ans([9], 1)
