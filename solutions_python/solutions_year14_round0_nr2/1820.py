i = 0
total = input()
answer_list=[]
while (i<total):
	inp= raw_input()
	lst = inp.split()
	cost_farm = float(lst[0])
	increase = float(lst[1])
	cost_final = float(lst[2])
	seconds = 0
	cookies_per_second = 2
	while(1):
		val = (cost_farm/cookies_per_second) + (cost_final/(cookies_per_second + increase))
		if cost_final/cookies_per_second > val:
	    		seconds += float(cost_farm/cookies_per_second)
	    		cookies_per_second +=increase    
		else:
	    		seconds += cost_final/cookies_per_second
	    		break
	answer_list.append(seconds)
	i+=1

i=0
while i<total:
	print "Case"+ " #"+str(i+1)+": "+str(answer_list[i])
	i+=1
