import os
import random

def read_input():
	file_name = "%s/large.in" % os.getcwd()
	return open(file_name, "r")

def get_ans(Smax, Slevels, num):
	ans = 0
	up_aud = 0
	for i in range(len(Slevels)):
		s = int(Slevels[i])
		# print "prev level=%d, up_aud=%d, ans=%d, amnt=%d" % (i, up_aud, ans, s)
		if i <= up_aud:
			up_aud += s
		elif s > 0:
			ans += i - up_aud
			up_aud += i - up_aud
			up_aud += s
		# print "post level=%d, up_aud=%d, ans=%d, amnt=%d" % (i, up_aud, ans, s)
	return "Case #%d: %d" % (num, ans)

def make_output(ans):
	file_name = "%s/large.out" % os.getcwd()
	f = open(file_name, "w")
	f.write(ans)
	f.close()

def main():
	ans = ""
	f = read_input()
	
	T = int(f.readline())
	for i in range(T):
		Smax, Slevels = f.readline().split()
		ans += get_ans(Smax, Slevels, i+1)
		if i < T-1: ans += "\n"

	f.close()
	make_output(ans)

main()
# print get_ans("4", "11111", 1)
# print get_ans("1", "09", 2)
# print get_ans("5", "110011", 2)
# print get_ans("0", "1", 2)



