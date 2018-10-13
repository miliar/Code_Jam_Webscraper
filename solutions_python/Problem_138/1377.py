#python3.4

from collections import deque

for N in range(int(input())):
	l = int(input())
	naomi_original = sorted( [float(n) for n in input().split()] )
	ken_original   = sorted( [float(n) for n in input().split()] )
	
	# start with normal wins
	
	w = 0  # No. Naomi war wins
	naomi = deque(sorted(naomi_original))
	ken   = deque(sorted(ken_original))
	for _ in range(l):
		if naomi[-1] > ken[-1]:
			w += 1
			naomi.pop()
			ken.popleft()
		else:
			naomi.pop()
			ken.pop()
	
	# now do deceitful war
	
	dw = 0  # No. Naomi deceitful war wins
	naomi = deque(sorted(naomi_original))
	ken   = deque(sorted(ken_original))
	for _ in range(l):
		# if heaviest ken is heavier than heaviest naomis
		if ken[-1] > naomi[-1]:
			# use lightest naomis to pop it
			naomi.popleft()
			ken.pop()
		else:
			break
	# now ken does not have a heavier brick than naomis heaviest
	# lets use that to our advantage
	while naomi:
		if naomi[0] < ken[0]:
			# naomi has the lightest brick
			# say it is almost as heavy as kens heaviest
			# then he has to use his heaviest while naomi uses her lightest
			# naomi didn't get a point but she got rid of one of kens big bricks
			naomi.popleft()
			ken.pop()
		else:
			# naomis lightest is bigger than kens lightest
			# say it is heavier than his heaviest
			# he uses his lightest which is indeed lighter
			dw += 1
			naomi.popleft()
			ken.popleft()
	
	print("Case #%d: %d %d" % (N+1, dw, w ))
