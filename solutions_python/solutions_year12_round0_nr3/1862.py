
# def test(a, b):
	# do nothing

def count(s1, s2):
	ans = [];
	a = int(s1); b = int(s2)
	for i in range(a,b+1):
		leng = len(s1);
		if leng<2: break;
		
		for j in range(leng):
			s = str(i);
			st = s[-j:]+s[:-j]
			num = int( st );
			# print i, num
			if num<=b and num>i: 
				# print i, num
				hash=str(i)+str(num);
				if hash not in ans: ans.append(hash)
				# ans+=1;
		
	return len(ans); 
	
t = int(raw_input());
for i in range(t):
	input = raw_input().split(' ');
	print 'Case #{}: {}'.format(i+1, count(input[0],input[1]) );