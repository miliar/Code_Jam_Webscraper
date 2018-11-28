#!/usr/bin/env python

def main():
	f = open('input.txt', 'r')

	total_T = int(f.readline())

	for T in xrange(1,total_T+1):
		N = map(long, f.readline().rstrip('\n').split())
		Naomi = sorted(map(float, f.readline().rstrip('\n').split()))
		Ken = sorted(map(float, f.readline().rstrip('\n').split()))

		# print N
		# print Naomi
		# print Ken

		# print war(Naomi, Ken)
		# print de_war(Naomi, Ken)



		# print E,R,N
		# print v

		print 'Case #{}: {} {}'.format(T, de_war(Naomi, Ken), war(Naomi, Ken))

def war(Naomi, Ken):
	s = 0
	while Naomi!=[]:
		n = Naomi[0]
		k = None
		for kk in Ken:
			if kk>n:
				k = kk
				break
		k = kk if kk else Ken[0]

		Naomi = Naomi[1:]
		Ken = filter(lambda x:x!=k, Ken)
		ss = 1 if n>k else 0
		s+=ss

	return s


	# if Naomi==[]:
	# 	return 0
	# n = Naomi[0]
	# k = None
	# for kk in Ken:
	# 	if kk>n:
	# 		k = kk
	# 		break
	# k = kk if kk else Ken[0]

	# Naomi_new = Naomi[1:]
	# Ken_new = filter(lambda x:x!=k, Ken)
	# s = 1 if n>k else 0
	# return s+ war(Naomi_new, Ken_new)

def de_war(Naomi, Ken):
	
	s = 0
	while Naomi!=[]:

		n = Naomi[0]
		if n < Ken[0]:
			k = Ken[-1]
		else:
			k = Ken[0]

		Naomi = Naomi[1:]
		Ken = filter(lambda x:x!=k, Ken)
		ss = 1 if n>k else 0
		s += ss
	return s

	# if Naomi==[]:
	# 	return 0

	# n = Naomi[0]
	# if n < Ken[0]:
	# 	k = Ken[-1]
	# else:
	# 	k = Ken[0]

	# Naomi_new = Naomi[1:]
	# Ken_new = filter(lambda x:x!=k, Ken)
	# s = 1 if n>k else 0
	# return s+ de_war(Naomi_new, Ken_new)


if __name__ == '__main__':
	main()