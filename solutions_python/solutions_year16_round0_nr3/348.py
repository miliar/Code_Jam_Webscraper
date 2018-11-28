import random
import math
import string


def translate_num(jamcoin,base):
	res = 0;
	for i in range(len(jamcoin)):
		res = res * base
		res = res + jamcoin[i];
	return res

def generate_jamcoin(length):
	jamcoin = [random.choice([0,1]) for i in range(length)]
	jamcoin[0] = 1
	jamcoin[-1] = 1
	return jamcoin

primetable1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
primetable100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


#def findfactor(largenum):
#	if(largenum > 994009):
#		examtable = primetable1000 + xrange(1001,(int(math.sqrt(largenum))+1))
#	else:
#		if(largenum > 9409):
#			examtable = primetable100 + xrange(101,(int(math.sqrt(largenum))+1))
#		else:
#	for i in examtable:
#		if (largenum % i) == 0:
#			return i
#	return 0

def findfactor(largenum,length,base):
	i = 3
	threshold = translate_num([1 for i in range((length/2)+1)],base)
	while(True):
	#for i in xrange(3,translate_num([1 for i in range(length+1)],base),2):
		if (largenum % i) == 0:
			return i
		i = i + 2
		if (i > threshold):
			break		
	return 0


def output(res,length):
        jamcoin = res[0:length]
        factors = res[length:]
        no_blank = ""
        blank = " "
        jamcoin_s = []
        factors_s = []
        for i in jamcoin:
                if (i == 1):
                        jamcoin_s.append('1')
                else:
                        jamcoin_s.append('0')
        for i in factors:
                factors_s.append("%d" %i)
        jamcoin_str = no_blank.join(jamcoin_s)
        factors_str = blank.join(factors_s)
        print jamcoin_str + " " + factors_str


def transint(num,base):
	a = []
	while(num != 0):
		a.append(num%base)
		num = num / base
	a.reverse()
	return a
def min_jam(length):
	return (2 ** (length-1)) + 1

def max_jam(length):
	return (2 ** length) - 1

def solve(length,number):
	examined = set()
	got = 0
	while (got < number):
		cc_list = generate_jamcoin(length / 2)
		cc = translate_num(cc_list,2)
		mult = 2**16 + 1
		jamcoin_num = cc * mult
		if (jamcoin_num in examined):
			continue
		examined.add(jamcoin_num)
		jamcoin_list = transint(jamcoin_num,2)
		factors = []
		no_blank = ""
		cc_lists = []
		for i in cc_list:
			if (i == 1):
				cc_lists.append('1')
			else:
				cc_lists.append('0')
		for i in range(2,11):
			factors.append(int(no_blank.join(cc_lists),i))
		output(jamcoin_list + factors,length)
		got = got + 1


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  print "Case #{}:".format(i)
  solve(n,m)
