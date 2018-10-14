# -*- coding: utf-8 -*-

import sys

class Recycle:
	def solve(self,low,high):		
		ans=0
		for offset in range(high+1-low):
			num = low+offset
			
			num_str = list("%d"%num)
			
			for i in range(len(num_str)-1):
				modified_str_list = num_str[i+1:] + num_str[0:i+1]
				if modified_str_list[0] == '0':
					continue
				else:
					modified_str = "".join(modified_str_list)
					modified_num = int(modified_str)
					if num != modified_num and modified_num >= low and modified_num <= high:
						ans+=1
		#print ans_dict
		return ans/2
		
recycle=Recycle()

f=open(sys.argv[1])
f2=open(sys.argv[2],'w')

lines=f.read().split('\n')

for idx in range(int(lines[0])):
	params = [int(param) for param in (lines[idx+1]).split(' ')]
	low=params.pop(0)
	high=params.pop(0)
	ans = recycle.solve(low,high)
	f2.write("Case #%d: %d\n"%(idx+1,ans))
f2.close
