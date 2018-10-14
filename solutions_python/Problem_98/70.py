# -*- coding: utf-8 -*-

import sys
import math
class Mirror:
	
	def propagate(self,r_x,r_y,v_x,v_y):
		#print "prop called. v_x:%f, v_y:%f"%(v_x,v_y)
		# window: (r_x,r_y) 内のperson pointを、
		#	next_window : (r_x+v_x,r_y+v_y) へと鏡映させる

		h = self.h
		w = self.w

		window_id="%d_%d"%(r_x,r_y)
		cur_c_x, cur_c_y = self.person_dict[window_id]
		
		#print "cur_c_x:%f,cur_c_y:%f"%(cur_c_x, cur_c_y)
				
		next_window_id="%d_%d"%(r_x+v_x,r_y+v_y)
		
		if v_x != 0 and v_y == 0:
			if v_x > 0:
				n_x = w*(r_x+v_x)
			else:
				n_x = w*r_x
				
			new_c_y = float(cur_c_y)
			new_c_x = float(cur_c_x) + 2.0 * v_x * math.fabs(n_x - float(cur_c_x))

		elif v_y != 0 and v_x == 0:
			if v_y > 0:
				n_y = h*(r_y+v_y)
			else:
				n_y = h*r_y
			
			
			new_c_x = cur_c_x
			new_c_y = cur_c_y + 2.0 * v_y * math.fabs(n_y - cur_c_y)

		#print "%d and %d"%(r_x+v_x,r_y+v_y)			
		#print "new_c_x:%f,new_c_y:%f\n"%(new_c_x,new_c_y)
			
		self.person_dict[next_window_id] = [new_c_x,new_c_y]

	
	def solve(self,h_org,w_org,d,p_x,p_y):
		#print "p_x:%f,p_y:%f"%(p_x,p_y)
		ans = 0
		self.h = h_org - 2.0
		self.w = w_org - 2.0
		
		c0_x, c0_y = [p_x+0.5,p_y+0.5]

		#print "c0_x:%f,c0_y:%f"%(c0_x,c0_y)
		
		self.person_dict={}
		self.person_dict['0_0']=[c0_x, c0_y]
		
		for a_x in range(0,d+2):
			for dir_x in [1,-1]:
				for a_y in range(0,d+2):
					for dir_y in [1,-1]:
						r_x = dir_x * a_x
						r_y = dir_y * a_y
				
						for m_v in [[dir_x,0],[0,dir_y]]:
							mx,my = m_v
							self.propagate(r_x,r_y,mx,my)
	
	
		mirror_image = {}
	
		for window_id, point in self.person_dict.items():
			c_x,c_y = point
			
			l_x = float(c_x)-float(c0_x)
			l_y = float(c_y)-float(c0_y)
			
			dist = math.pow(l_x,2)+math.pow(l_y,2)
			
			if (dist <= math.pow(d,2) and dist>0):
				#print "c_x:%.3f,c_y:%.3f,window_id:%s,dist:%.3f"%(c_x,c_y,window_id,dist)
				if l_x == 0:
					if l_y > 0:
						ray_v = '0_1'
					else:
						ray_v = '0_-1'						
				elif l_y == 0:
					if l_x > 0:
						ray_v = '1_0'
					else:
						ray_v = '-1_0'						

				else:
					length = math.fabs(l_x)
					ray_v = '%.8f_%.8f'%(l_x/length,l_y/length)
					
				if not mirror_image.has_key(ray_v):
					mirror_image[ray_v]=dist
				
		#print mirror_image
		return len(mirror_image)
			
									
mirror=Mirror()

f=open(sys.argv[1])
f2=open(sys.argv[2],'w')

lines=f.read().split('\n')

testcase_num = int(lines[0])
start_idx=1

for idx in range(testcase_num):
	h,w,d = [int(param) for param in (lines[start_idx]).split(' ')]
	p_x,p_y = [-1,-1]
	start_idx+=2
	for j in range(h-2):
		p_x_cond = lines[start_idx].find('X')-1
		if(p_x_cond>=0):
			p_x = p_x_cond
			p_y = j
		start_idx+=1
	start_idx+=1
	
	ans = mirror.solve(h,w,d,float(p_x),float(p_y))
	f2.write("Case #%d: %d\n"%(idx+1,ans))
f2.close
