from __future__ import division
def nextbig(tot_dis, horse_arr):			
	new_times = []
	# create the times array 
	maxt = -1
	for i in range(len(horse_arr)): maxt = max((tot_dis - horse_arr[i][0]) / horse_arr[i][1], maxt)
	return tot_dis / maxt		
if __name__ == '__main__':
	f = open('out.out', 'w')
	with open('A-large.in', 'r') as fle:
		r = fle.readlines()
		t = int(r[0][:-1]) # number of testcases 
		z = 1 # first case 
		for i in range(1, t+1): # all testcases 
			l = r[z].split(' ') 
			tot_dis = int(l[0]) # total distance 
			num_horses = int(l[1]) # number of horses 
			z += 1 # initail placements begin 
			horse_arr = [] 
			for j in range(num_horses):
				ll = r[z].split(' ') 
				horse_arr.append([int(ll[0]), int(ll[1])])
				z += 1 

			yeah = nextbig(tot_dis, horse_arr)				
			f.write('Case #' + str(i) + ': '+ str(yeah) + '\n')						
		f.close()	 
	
		