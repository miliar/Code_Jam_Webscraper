import math,copy

sourceFile = "small.in";
outputFile = "small.out";

s_handler = open(sourceFile, 'r');
o_handler = open(outputFile, 'w');

T = s_handler.readline();

for i in range(1, int(T)+1):
	line = s_handler.readline().strip();
	bags_of_words = line.split(" ");
	A = int(bags_of_words[0]);
	B = int(bags_of_words[1]);

	possbility = [];
	line = s_handler.readline().strip();
	bags_of_words = line.split(" ");
	for j in range(0 , A):
		possbility.append( float(bags_of_words[j] ) );
	
	best = 100000;

	final_p = [];

	differentP = int(math.pow(2,A));
	for j in range(0, differentP):
		possbility2 = copy.deepcopy(possbility);
		binary = str( bin(j) )[2:];
		lack_len = A - len(binary);
		binary = "0" * lack_len + binary;
		#binary = binary[::-1];
		for kk in range(0, len(binary)):
		#	print str(j) + " " + str(kk) + " " + binary + " " + str(lack_len);
			if (binary[kk] == '1'):
				possbility2[kk] = 1 - possbility2[kk];
		po = 1;
		for m in range(0,A):
			po *= possbility2[m];
		final_p.append(po);
		#print po;
	
	#type 1,keep typing:
	first = B-A+1;
	second = 2*B-A + 2;

	tmp = 0;
	tmp += first * final_p[0];
	for m in range(1, differentP):

		tmp += second * final_p[m];
	if (tmp < best):
		best = tmp;
	#print "tmp:" + str(tmp);
	
	#type 2, backspace

	for s in range(1, A+1):
		tmp = 0;
		for ss in range(0, differentP):
			binary = str( bin(ss) )[2:];
			if (len(binary) <= s):
				times = s + s + B - A + 1;
			else:
				times = s + s + 2*B - A + 2;

			tmp += times * final_p[ss];

		if (tmp < best):
			best = tmp;
				
		#print "tmp:" + str(tmp);

	#type 3, press enter
	times = B + 2;
	tmp = 0;
	for m in range(0, differentP):
		tmp += times * final_p[m];
	if (tmp < best):
		best = tmp;
	#print "tmp:" + str(tmp);
	
	#print best;
		
		
	o_handler.write("Case #" + str(i) + ": " + str(best) + "\n");
	#print "---";

s_handler.close();
o_handler.close();
