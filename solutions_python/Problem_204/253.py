import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	n_ingredients = int(line.split(' ')[0])
	p_packages = int(line.split(' ')[1])
	
	line = in_file.readline().replace('\n', '')
	one_serving_grams = line.split(' ')
	i = 0
	while(i < len(one_serving_grams)):
		one_serving_grams[i] = int(one_serving_grams[i])
		i += 1
	
	package_grams = []
	i = 0
	while(i < n_ingredients):
		line = in_file.readline().replace('\n', '')
		package_grams.append(line.split(' '))
		j = 0
		while(j < len(package_grams[i])):
			package_grams[i][j] = int(package_grams[i][j])
			j += 1
		i += 1
	
	# Sort the packages of the same ingredients
	i = 0
	while(i < n_ingredients):
		package_grams[i].sort()
		i += 1
	
	# ROUND(SUM(package[i] / one_serving_grams[i]) / i) = serving to try
	#print(one_serving_grams)
	#print(package_grams)
	
	p_indexes = []
	i = 0
	while(i < n_ingredients):
		p_indexes.append(0)
		i += 1
	
	valid_packages = 0
	done = False
	while(not done):
		i = 0
		sum = 0
		while(i < n_ingredients):
			pg = package_grams[i][p_indexes[i]]
			pg_ratio = float(pg) / float(one_serving_grams[i])
			sum += pg_ratio
			i += 1
		serving_attempt = int(round(sum / n_ingredients))
		#print(serving_attempt)
		valid = True
		i = 0
		while(i < n_ingredients):
			pg = package_grams[i][p_indexes[i]]
			sg = (one_serving_grams[i] * serving_attempt)
			if (pg < (0.9 * sg)):
				valid = False
				break
			elif ((1.1 * sg) < pg):
				valid = False
				break
			i += 1
		if(valid):
			valid_packages += 1
			# clear taken packages
			i = 0
			while(i < n_ingredients):
				package_grams[i][p_indexes[i]] = -1337
				i += 1
		# increment the package indexes
		x = n_ingredients - 1
		added = False
		while((not added) and (x > -1)):
			p_indexes[x] += 1
			if(p_indexes[x] >= p_packages):
				p_indexes[x] = 0
				x -= 1
			else:
				# Check for slot as anything but -1337
				#if(package_grams[x][p_indexes[x]] != -1337):
					#added = True
				added = True
		if(not added):
			done = True
	
	out_file.write(str(valid_packages))
	out_file.write('\n')
	
if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()