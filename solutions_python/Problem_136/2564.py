#Magician
import string;

epsilon = pow(10,-6);

def cookie(C,F,X):
	result = 0;
	rate = 2.0;
	n = 0;
	if (X < C):
		result = X/rate;
	else:
		next = min(X/rate, C/rate + X/(rate+F));
		while (next == C/rate + X/(rate+F)):
			result = result + C/rate;
			rate = rate + F;
			next = min(X/rate, C/rate + X/(rate+F));
			n = n + 1;
		result = result + X/rate;
	return result;


#main program

#read file
# infile = open('input_small.in');
infile = open('B-large.in','r');
outfile = open('output.out','w');

#read case
cases = int(infile.readline().rstrip());

i = 1;
while (i <= cases):
	rows = infile.readline().rstrip().split();
	C = float(rows[0]);
	F = float(rows[1]);
	X = float(rows[2]);

	result = cookie(C,F,X);

	outfile.write("Case #" + str(i) + ": " + str(result) + '\n');

	i = i + 1;

infile.close();
outfile.close();