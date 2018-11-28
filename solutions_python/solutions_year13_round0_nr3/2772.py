import sys
import gmpy2
from gmpy2 import mpz

file = open("C-small-attempt0.in")

inputs = []

while 1:
    line = file.readline()
    if not line:
        break
    inputs.append(line)

for i in xrange(len(inputs)-1):
	inputs[i] = inputs[i][:-1].split()

inputs[len(inputs)-1] = inputs[len(inputs)-1].split()

num_intervals = int(inputs[0][0])


def is_pal(str_num):
	for i in xrange(len(str_num) / 2):
		if str_num[i] !=  str_num[-(i+1)]:
			return False
	return True

def find_pals(a,b):
	pals = []
	for i in xrange(long(a),long(b)+1):
		if is_pal(str(i)):
			pals.append(i)
	return pals

# def is_square(str_num):
# 	(s,t) = gmpy2.isqrt_rem(mpz(str_num))
# 	return (t == 0)

def counf_fs(a,b):
	((sa,ta),(sb,tb)) = (gmpy2.isqrt_rem(mpz(a)),gmpy2.isqrt_rem(mpz(b)))
	if (ta == 0):
		min_root = sa
	else:
		min_root = sa + 1
	max_root = sb
	root_pals = []
	for i in xrange(min_root,max_root+1):
		if is_pal(str(i)):
			root_pals.append(i)
	num_fs = 0
	for root_pal in root_pals:
		if is_pal(str(mpz(root_pal)*mpz(root_pal))):
			num_fs += 1
	return num_fs

	# for i in xrange()

	# pals = find_pals(a,b)
	# print pals
	# num_fs = 0
	# for pal in pals:
	# 	if is_square(pal):
	# 		print pal
	# 		num_fs += 1
	# return num_fs

# print inputs
text_file = open("CSmallOutput.txt", "w")


for (i,[a,b]) in enumerate(inputs[1:]):
	tex = ("Case #"+str(i+1)+": "+str(counf_fs(a,b))+"\n")
	text_file.write("%s"%tex)

text_file.close()

