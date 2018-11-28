# Problem D. Deceitful War
#
# Author: Phuriphat Boontanon
import sys

if not len(sys.argv):
	sys.exit()

input = open(sys.argv[1])
T = int(input.readline())
for k in range(1, T+1):
	n = int(input.readline())
	naomi_n = [float(x) for x in input.readline().split()]
	ken_n = [float(x) for x in input.readline().split()]
	naomi_n.sort()
	ken_n.sort()
	naomi_d = naomi_n[::]
	ken_d = ken_n[::]
	naomi_points_d = 0
	ken_points_d = 0
	naomi_points_n = 0
	ken_points_n = 0
	while n:
		# deceitful 
		if naomi_d[-1] < ken_d[-1]:
			naomi_d.pop(0)
			ken_d.pop(-1)
		else:
			for i in range(0, len(naomi_d)):
				if naomi_d[i] > ken_d[0]:
					ken_d.pop(0)
					naomi_d.pop(i)
					naomi_points_d += 1
					break
			
		#normal
		if naomi_n[-1] > ken_n[-1]:
			# naomi win
			naomi_points_n += 1
			ken_n.pop(0)
			naomi_n.pop(-1)
		else:
			# ken win
			ken_points_n += 1
			ken_n.pop(-1)
			naomi_n.pop(-1)
		n = n-1
	print 'Case #%d: %d %d'%(k, naomi_points_d, naomi_points_n)