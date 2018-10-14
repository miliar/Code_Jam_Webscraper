import math
from fractions import Fraction

def n_turns(h_d,a_d,h_k,a_k,b,d,buff_count,debuff_count):
	cur_h_d = h_d
	cur_h_k = h_k
	cur_a_d = a_d
	cur_a_k = a_k
	
	turns = 0
	
	for _ in range(debuff_count):
		if cur_h_d - (cur_a_k - d) <= 0:
			turns += 1
			cur_h_d = h_d
			cur_h_d -= cur_a_k
		
		cur_a_k -= d
		if cur_a_k < 0: cur_a_k = 0
		
		cur_h_d -= cur_a_k
		
		turns += 1
		
		if cur_h_d <= 0:
			return None
		
	for _ in range(buff_count):
		if cur_h_d - cur_a_k <= 0:
			turns += 1
			cur_h_d = h_d
			cur_h_d -= cur_a_k
			
		cur_a_d += b
		cur_h_d -= cur_a_k
		
		turns += 1
		
		if cur_h_d <= 0:
			return None
	
	
		
	did_cure = False
	while True:
		#print cur_h_k, cur_h_k
		if cur_h_k - cur_a_d <= 0:
			turns += 1
			#print 'finish'
			
			return turns
	
		if cur_h_d - cur_a_k <= 0:
			#if did_cure:
			#	print 'no!'
			#	return None
		
			turns += 1
			cur_h_d = h_d
			cur_h_d -= cur_a_k
			
			#print 'cure'
			
			did_cure = True
		else:
			did_cure = False
		
		cur_h_k -= cur_a_d
		cur_h_d -= cur_a_k
		
		
		if cur_h_d <= 0:
			return None
		
		turns += 1
	
	
		

def solve(h_d,a_d,h_k,a_k,b,d):
	best = None

	for buff_count in range(0,101):
		for debuff_count in range(0,101):
	
			cur = n_turns(h_d,a_d,h_k,a_k,b,d,buff_count,debuff_count)
			if cur != None and (best == None or cur < best):
				best = cur
				#print buff_count,debuff_count
	
	if best == None:
		print 'IMPOSSIBLE'
	else:
		print best

def nope_solve(h_d,a_d,h_k,a_k,b,d):

	if b:
		float_buff_count = ((h_k*b)**0.5 - a_d) / float(b)
		
		approx_buff_count = int(float_buff_count)
	
		buff_count = None
		min_turns = None
		
		for i in range(-1,1):
			potential_buff_count = approx_buff_count + i
			if potential_buff_count < 0:
				potential_buff_count = 0
			cur_turns = Fraction(h_k, (b*potential_buff_count + a_d)) + potential_buff_count
			cur_turns = int(math.ceil(cur_turns))
			
			if min_turns == None or cur_turns < min_turns:
				min_turns = cur_turns
				buff_count = potential_buff_count
		
	else:
		buff_count = 0
	
	attack_turns = Fraction(h_k, (b*buff_count + a_d)) + buff_count
	attack_turns = int(math.ceil(attack_turns))
	
	print buff_count,attack_turns
	
	


case_count = input()
for case in range(1,case_count+1):
	print 'Case #%d:' % case,
	
	h_d,a_d,h_k,a_k,b,d = map(int,raw_input().split(' '))
	
	solve(h_d,a_d,h_k,a_k,b,d)