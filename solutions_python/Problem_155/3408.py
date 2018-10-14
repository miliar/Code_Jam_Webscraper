fin = open("input",'r');
fout = open("out1",'w');
tc = int(fin.readline())+1;
for cn in range(1,tc):
	line = fin.readline().split(" ");
	smax = int(line[0])+1;
	psl = line[1];
	req = 0;
	standing = 0;
	for i in xrange(0,smax):
		if i > standing:
			req = req + 1;
			standing = standing + 1;
		standing = standing + int(psl[i]);
	fout.write("Case #"+`cn`+": "+`req`+"\n");
	
