
from fractions import gcd;


def doit(R, K, N, lst):
	
	if R == 0:
		return 0;
	
	i = 0;
	while i < N:
		lst[i] = int(lst[i]);
		i = i + 1;
		
	fee = 0;
	times = 0;
	head = 0;		# points to queue head
	
	while 1:
		if head == 0 and fee != 0:
			break;
		
		mark = head;	
			
		p = 0;
		
		while 1:	# boarding
			if (mark == head and p != 0) or (p + lst[head] > K):	# full
				times = times + 1;
				break;
			p = p + lst[head];
			fee = fee + lst[head];
			head = head + 1;
			if head == N:
				head = 0;
		
		if times == R:
			return fee;
			
	# $times is a loop, fee
	return int((R - R%times) / times * fee) + doit(R%times, K, N, lst);

def main():
	c = input();
	i = 1;
	while i <= int(c):
		st = input();
		lst = st.split();
		R = int(lst[0]);
		K = int(lst[1]);
		N = int(lst[2]);
		
		st = input();
		lst = st.split();
		print('Case #' + str(i) + ': ' + str(doit(R, K, N, lst)));
		i = i + 1;
	
main();
