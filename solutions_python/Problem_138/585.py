#gc Minesweeper Master
import string
from math import *
from copy import copy

if __name__ == "__main__":
	input = open('D-large.in')
	output = open('war_output.txt','w')
	
	T = int(input.readline().replace('\n',''))
	
	#War points
	for i in xrange(1, T+1):
		N = int(input.readline().replace('\n',''))
		naomi = sorted([float(k) for k in input.readline().replace('\n','').split(' ')])
		ken = sorted([float(k) for k in input.readline().replace('\n','').split(' ')])
		
		ken_war = copy(ken)
		non_optimal = optimatl = ken_points = naomi_points = 0
		for j in naomi:
			m = min(ken_war, key=lambda x: abs(j-x) if j<=x else float('inf'))
			if m < j: 
				naomi_points+=1
				m = min(ken_war)
			else:
				ken_points+=1
			del ken_war[ken_war.index(m)]
		
		ken_deceit_points = naomi_deceit_points = 0
		naomi_deceit = copy(naomi)
		while naomi_deceit:
			m = ken.pop()
			end_elem = naomi_deceit[-1]
			if m > end_elem:
				del naomi_deceit[0]
				ken_deceit_points+=1
			else:
				naomi_deceit.pop()
				naomi_deceit_points+=1
				
		output.write("Case #%d: %d %d\n" % (i,naomi_deceit_points,naomi_points))
	
	input.close()
	output.close()