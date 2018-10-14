import sys

sys.stdin = open("in.txt", 'r')
sys.stdout = open("out.txt", 'w')

num = input()


def check_tidy(st):
	for x in range(0, len(st) - 1):
		if int(st[x]) > int(st[x+1]):
			return False
	return True

def make_tidy(st):
	for x in range(0, len(st) - 1):
		if int(st[x]) > int(st[x+1]):
			st_new = st[:x] + str(int(st[x]) - 1) + "9"*(len(st) - x - 1)
			break
	# remove trailing zeros.
	ind = 0
	while st_new[ind] == "0":
		ind += 1
	st_new = st_new[ind:]
	return st_new


#while not check_tidy(st):
#	st = make_tidy(st)

casenum = 1
for i in range(0, int(num)):
	st = input()
	if len(st) > 1:
		while not check_tidy(st):
			st = make_tidy(st)
	print("Case #" + str(casenum) + ": " + st)
	casenum += 1