import copy

infile = open('D-large.in','r')
outfile = open('out.txt','w')
tests = int(infile.readline())


for i in range(tests):
    naomi = []
    ken = []
    N = int(infile.readline())
    numbers = infile.readline().split()

    for j in range(N):
	naomi.append(float(numbers[j]))

    numbers = infile.readline().split()

    for j in range(N):
	ken.append(float(numbers[j]))

    naomi.sort()
    naomi_sorted = copy.copy(naomi)
    naomi.reverse()
    ken.sort()
    ken_dsorted = copy.copy(ken)
	
    war_points = 0
    dwar_points = 0

    #print naomi
	
    length = N
    for n_el in naomi:
	if (n_el > ken[length-1]):
		war_points = war_points + 1
	        element = ken.pop(0)
		#print ken
	else:
		ken_cp = copy.copy(ken)
		for ken_el in ken_cp:
			if (n_el < ken_el):
				ken.remove(ken_el)
				break
	#	print ken
	length = length - 1

    for ken_el in ken_dsorted:
	for n_el in naomi_sorted:
	    if (n_el > ken_el):
		dwar_points = dwar_points + 1
		naomi_sorted.remove(n_el)
		break

    outfile.write('Case #'+ str(i+1)+': ' + str(dwar_points) + ' ' + str(war_points) +'\n')

infile.close()
outfile.close()

