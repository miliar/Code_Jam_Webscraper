
inputfile = 'D-large.in'
outputfile = 'outputfile.txt'

fi = open(inputfile)
fo = open(outputfile, 'w')

test_cases = int(fi.readline())
print test_cases
for case in range(test_cases):
	N = int(fi.readline())
	line = fi.readline()
	line = line.strip('\n')
	naomi = map(float, line.split(' '))
	naomi.sort()
	naomi_1 = map(float, line.split(' '))
	naomi_1.sort()

	line = fi.readline()
	ken = map(float, line.split(' '))
	ken.sort()
	ken_1 = map(float, line.split(' '))
	ken_1.sort()
	naomi_score = 0
	ken_score = 0
	naomi_deceit_score = 0
	ken_deceit_score = 0

	for i in range(N):
		naomi_chosen = naomi[i]
		ken_may = [j for j in ken if j >= naomi_chosen]
		if len(ken_may) > 0:
			ken_chosen = ken_may[0]
		else:
			ken_chosen = ken[0]
		ken.remove(ken_chosen)
		if naomi_chosen > ken_chosen:
			naomi_score = naomi_score +1		
		else:
			ken_score = ken_score+1

		
		ken_small = min(ken_1)
		naomi_may_1 = [j for j in naomi_1 if j >= ken_small]
		
		if len(naomi_may_1) > 0:
			naomi_chosen_1 = naomi_may_1[0]
			naomi_told = max(ken_1) + 0.0000001
		else:
			naomi_chosen_1 = min(naomi_1)
			naomi_told = max(ken_1) - 0.0000001
		
		naomi_1.remove(naomi_chosen_1)

		ken_may_1= [j for j in ken_1 if j >= naomi_told]
		if len(ken_may_1) > 0:
			ken_chosen_1 = ken_may_1[-1]
		else:
			ken_chosen_1 = ken_1[0]
		ken_1.remove(ken_chosen_1)

		if naomi_chosen_1 > ken_chosen_1:
			naomi_deceit_score = naomi_deceit_score + 1
		else:
			ken_deceit_score =  ken_deceit_score + 1

	fo.write('Case #' + str(case+1) + ': ' + str(naomi_deceit_score) + ' ' +  str(naomi_score) + '\n')


fi.close()
fo.close()
		
