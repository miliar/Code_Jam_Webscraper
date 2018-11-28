import sys;

ip_f = open(sys.argv[1], 'r')

T = int(ip_f.readline());

for i in range(T):
	ans_1 = int(ip_f.readline());
	config_1 = [];
	for j in range(4):
		config_1.append(list(map(int,ip_f.readline().split())));

	ans_2 = int(ip_f.readline());
	config_2 = [];
	for j in range(4):
		config_2.append(list(map(int,ip_f.readline().split())));
	
	matches = 0;
	lastmatch = 0;
	for j in range(4):
		for k in range(4):
				if (config_1[ans_1-1][j] == config_2[ans_2-1][k]):
					last_match = config_1[ans_1-1][j];
					matches = matches+1;
	
	if (1 == matches):
		print('Case #%d: %d' % (i+1, last_match) );
	elif (0 == matches):
		print('Case #%d: Volunteer cheated!' % (i+1));
	else:
		print('Case #%d: Bad magician!' % (i+1));
