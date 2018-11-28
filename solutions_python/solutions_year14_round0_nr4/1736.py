import math
case_num = int(raw_input())
for i in xrange(1, case_num+1):
	print 'Case #%d:'%i,
	N= int(raw_input())
	naomi = [(float(x),'n') for x in raw_input().split()]
	ken = [(float(x),'k') for x in raw_input().split()]
	mixed = naomi+ken
	mixed.sort()
	#print mixed
	n_honest_war = 0
	k_deceit_war = 0
	k_deceit_war1 = 0
	k_deceit_war2 = 0
	flag_for2 = 0
	for j in range (0, 2*N):
		#print "--->", mixed[j],
		if mixed[j][1] == 'k':
			if n_honest_war > 0:
				n_honest_war-=1
			k_deceit_war1 += 1
			flag_for2 = 1
			k_deceit_war+=1
		if mixed[j][1] == 'n':
			n_honest_war +=1
			k_deceit_war1 = 0
			if flag_for2 == 0:
				k_deceit_war2 += 1
			if k_deceit_war >0:
				k_deceit_war-=1
	#print "-->",k_deceit_war1,k_deceit_war2
	#n_deceit_war = N- max(k_deceit_war1, k_deceit_war2 )
	n_deceit_war = N- k_deceit_war
	print n_deceit_war, n_honest_war