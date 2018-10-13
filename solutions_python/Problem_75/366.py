import sys;

f_ip = open(sys.argv[1],'r');
T = int(f_ip.readline());

for case in range(T):

#	print "--";
	input = f_ip.readline().split();
	input.reverse();
	
	combiMap = {
		'Q':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'W':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'E':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'R':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'A':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'S':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'D':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''}),
		'F':dict({'Q':'', 'W':'', 'E':'', 'R':'', 'A':'', 'S':'', 'D':'', 'F':''})
	}
	
	oppositionMap = {
		'Q':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'W':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'E':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'R':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'A':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'S':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'D':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False}),
		'F':dict({'Q':False, 'W':False, 'E':False, 'R':False, 'A':False, 'S':False, 'D':False, 'F':False})
	}


	C = int(input.pop());
	for combi in range(C):
		production = input.pop();
		combiMap[production[0]][production[1]] = production[2];
		combiMap[production[1]][production[0]] = production[2];

	D = int(input.pop());
	for oppi in range(D):
		production = input.pop();
		oppositionMap[production[0]][production[1]] = True;
		oppositionMap[production[1]][production[0]] = True;

	N = int(input.pop());
	testString = input.pop();

	result = [];

	for pointer in range(N):	# Iterate over Test String
		result.append(testString[pointer]);
#		print result;
		if len(result) >=2:	# No todo for single element in list
			if result[-2] in combiMap:	# Last top of stack was a base
				if (combiMap[result[-1]][result[-2]] != ''):
					to_be_pushed = combiMap[result[-1]][result[-2]];
					result.pop();
					result.pop();
					result.append(to_be_pushed);
#					print result;
				else:	# No combination, search for opposition
					for iter in result:
						if iter in oppositionMap:
							if oppositionMap[iter][result[-1]]:
#								print result;					
								result = [];
								break;
			else:	# Last top of stack was a non-base
				for iter in result:
					if iter in oppositionMap:
						if oppositionMap[iter][result[-1]]:
#							print result;					
							result = [];
							break;
				
	print "Case #" + str(case+1) + ":",
	print str(result).replace('\'','');
