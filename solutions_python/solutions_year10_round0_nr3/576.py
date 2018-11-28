#! /usr/bin/python

__author__ = "assim"
__date__ = "$May 8, 2010 9:10:51 AM$"



def solve(num_rides, capacity, num_grp, grp_list):
	filled_que = []
	money_made = 0
	for k in xrange(num_rides):
		filled = 0
		grp_list.extend(filled_que)
		filled_que = []
		#print "start", filled_que, grp_list
		while grp_list:
			if filled + grp_list[0] > capacity:
				break
			filled_que.append(grp_list.pop(0))
			#print filled_que, grp_list
			filled += filled_que[-1]
		#print "final", filled_que, grp_list
		money_made += filled
	return money_made
	
def parse(p = "c-s"):
	input = open("%s-i" %(p), "r")
	output = open("%s-o"%(p), "w")
	output_str_list = []
	num_cases = int(input.readline())
	for case in xrange(num_cases):
		num_rides, capacity, num_grp = input.readline().split()
		grp_list = [int(k) for k in input.readline().split()]
		money_made = solve(int(num_rides), int(capacity), int(num_grp), grp_list)
		output_str_list.append("Case #%s: %s" % (case + 1, money_made))
		#output.write("Case #%s: %s" % (case + 1, solve(int(n), int(k))))
		#output.write("\n")
	input.close()
	output.write("\n".join(output_str_list))
	output.close()







if __name__ == "__main__":
	parse()
	#print solve(num_rides = 4,
	#		capacity = 6,
	#		num_grp = 4,
	#		grp_list = [1,4,2,1])

