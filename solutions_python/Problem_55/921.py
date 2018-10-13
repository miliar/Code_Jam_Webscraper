f = open('themeparksmall.in', 'r')
out = open('themeparksmall.out', 'w')

cases = int(f.readline())

for i in range(cases):	
	li = f.readline().replace("\n", "").split(" ")
	
	money = 0
	num_runs = int(li[0])
	peo_per_run = int(li[1])
	num_of_groups = int(li[2])
	
	groups = f.readline().replace("\n", "").split(" ")
	
	g = 0
	
	for j in range(num_runs):
		
		start_index = g
		x = 1
		people_this_run = 0
	
		while people_this_run <= peo_per_run:
			if start_index == g:
				if x == 1:
					x = 2
					pass
				else:
					x = 1
					break
			if int(groups[g]) + people_this_run <= peo_per_run:
				people_this_run = people_this_run + int(groups[g])
				money = money + int(groups[g])
				if ( g == len(groups) - 1):
					g = 0
				else:
					g = g + 1
					
			else:
				break;
	
	outline = "Case #%d: %d\n" % (i + 1, money)
	print outline
	out.write(outline)

#out.close()	
f.close()
