inn = open('in','r')
f = open('out','w')
case = int(inn.readline().strip())

table = {('i','j'):'k',
	 ('i','i'):'-1',
         ('i','k'):'-j',
         ('j','i'):'-k',
         ('j','k'):'i',
         ('j','j'):'-1',
         ('k','i'):'j',
	 ('k','j'):'-i',
         ('k','k'):'-1',
         ('1','i'):'i',
         ('1','j'):'j',
         ('1','k'):'k'}

def multiply(m1,m2):
	if len(m1) == 1 and len(m2) == 1:
		return table[(m1,m2)]
	elif len(m1) == 2 and len(m2) == 2:
		return table[(m1,m2)]
	else:
		res = table[(m1[len(m1)-1],m2[len(m2)-1])]
                if len(res) == 2:
			return res[1]
		else:
			return '-'+res

from collections import deque
for case_num in range(case):
	l,x = [int(x) for x in inn.readline().strip().split()]
	s = deque(inn.readline().strip() * x)
	cur = s.popleft()
	found_i = False
	found_j = False
	while len(s)!= 0:
		if not found_i:
			if cur=='i':
				found_i = True
				cur = s.popleft()
				continue
		elif not found_j:
			if cur=='j':
				found_j = True
				cur = s.popleft()
				continue
		cur = multiply(cur,s.popleft())
	
	r = "NO"
        #print found_i,found_j, cur=='k'
	if found_i and found_j and cur=='k':
		r = "YES"
	w = "Case #"+str(case_num+1)+": "+r
	print w	
	f.write(w+'\n')

inn.close()
f.close()
