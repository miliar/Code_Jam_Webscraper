import sys
import csv

def stop_flip(str):
	## Returns boolean True if the string all '+', otherwise False
	out = True if str == '+'*len(str) else False
	return out

def flip(sec):
	# Returns flipped string
	fsec = ['-' if x=='+' else '+' for x in sec]
	return ''.join(fsec)

def fscan(str,char='-'):
	# Scans string until the firs occurence of char:
	out = None
	for ix, s in enumerate(str):
		if s == char:
			out = ix
			break
	return out
	
def stitch(s0, s1, pos):
	# Replaces a portion of s0 for s1 from position pos, with restriciton that it won't go over original s0 length
	if pos + len(s1)>len(s0):
		out = s0
	elif pos == 0:
		out = s1 + s0[pos+len(s1):]
	else:
		out = s0[:pos] + s1 + s0[pos+len(s1):]
	return out

def flip_counter(str,k):
	n_flips = 0
	s = len(str)
	k = int(k)
	if stop_flip(str):
		n_flips = 0
	elif str == '-'*s:
		if s % k !=0:
			f_point = 0
			while (stop_flip(str)==False and f_point+k<s):
				f_point = fscan(str)
				if len(str[f_point:f_point+k])<k:
					break
				else:
					flop = flip(str[f_point:f_point+k]) 
					str = stitch(str, flop, f_point)
					n_flips +=1
					## Just in case:
					if n_flips > len(str):
						break		
			if stop_flip(str) == False:
				n_flips = 'IMPOSSIBLE'
			
		else:		
			n_flips = int(s/k)
	else:
		f_point = 0
		while (stop_flip(str)==False and f_point+k<s):
			f_point = fscan(str)
			if len(str[f_point:f_point+k])<k:
				break
			else:
				flop = flip(str[f_point:f_point+k]) 
				str = stitch(str, flop, f_point)
				n_flips +=1
				## Just in case:
				if n_flips > len(str):
					break		
		if stop_flip(str) == False:
			n_flips = 'IMPOSSIBLE'
	return n_flips

f = open(sys.argv[1], 'r') 
n_cases = f.readline()
 
cnt = 0
for row in f:
	cnt +=1
	str,k = row.rstrip("\n\r").split(' ')
	out = flip_counter(str,k)
	print('Case #{}: {}'.format(cnt, out))