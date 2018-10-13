fi=open("B-large.in",'r')#Input File 
#fi=open("A-small-practice.in",'r')#Input File 
#fi=open("A.in",'r')#Input File 
fo=open("B-large.out","w")#Output File 
#fo=open("A-large-practice.out","w")#Output File 
T=int(fi.readline()) 
global score_list
score_list = []

def find(arr, new_arr, index, no):
	for i, n in enumerate(arr):
		new_arr[index] = n
		if sum(new_arr) == no:
			global score_list
			temp_arr = []
			temp_arr.extend( new_arr )
			score_list.append(temp_arr)			
			return
		if index == 2:
			return
		find(arr, new_arr, index+1, no)
	return

def find_3no(no):
	n1, rem = divmod( no, 3 )
	if n1 < 0:
		n1 = 0
	n2 = n1 + 1
	n3 = n1 + 2
	if rem == 0:
		n2 = n1 - 1
		n3 = n1 + 1

	arr = [n1, n2, n3]
	new_arr = [0, 0, 0]	
	find(arr, new_arr, 0, no)

def if_suprise(scores):
	scores.sort()	
	if scores[2]-scores[0] == 2 or scores[1]-scores[0] == 2 or scores[2]-scores[1] == 2: 
		return 1
	return 0
	
def find_atleast_p(p, s, scores):
	for score in scores:
		if score >= p:
			if if_suprise(scores): 
				if s:
					return 1, 1
				else:
					return 0, 0			
			else:			
				return 1, 0
			
	return 0, 0

for case in range(1,T+1,1): 
	line = fi.readline()
	nos = line.split()
	n, s, p = int(nos[0]), int(nos[1]), int(nos[2])
	ds = []	
	ans = 0

	for i in range(3, n+3):
		no = int(nos[i])
		find_3no(no)
		flag_p = 0
		flag_s = 0	
		p_with_s = 0
		#print score_list	
		
		for scores in score_list:
			p_state , s_state = find_atleast_p(p, s, scores)
			if p_state and s_state == 0:
				flag_p = 1
				flag_s = 0
				break
			if s_state and p_state:
				flag_s = 1		
				
			#if s_state == 0:
			#	flag_s = 1			
			
		if flag_p:				
			ans += 1
		if flag_s:
			s -= 1
			ans += 1

			
		score_list = []	
		#break
		
	fo.write("Case #"+str(case)+": "+str(ans)+"\n")
		
	
fi.close()
fo.close()	

