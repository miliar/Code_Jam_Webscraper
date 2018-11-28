##
workdir = "C:\codejam2014\\"
input_file = "B-large.in"
#input_file = "B-lrg-practice.in"
#print input_file.split(".")
output_file = input_file.split(".")[0] + ".out"
inp = workdir + input_file
outp = workdir + output_file
f = open(inp, 'rU')
g = open(outp, 'w')
T = int(f.readline())
case_size = 1
#print("#cases: ", T)
##
def GetBestTime(r, C, F, X):
	t = 0.0
	rate = r
	cookie_count = 0.0
	if C >= X:
		return (X/rate)
	else:
		while cookie_count < X:
			t = t + C/rate
			cookie_count = C
			if (X-C)/rate > X/(rate+F):
				cookie_count = 0.0
				rate = rate + F
			else:
				return (t + (X-C)/rate)




case_dict = {}
for case_index in range(T):
    line_dict = {}
    for line_index in range(case_size):
        line = f.readline()
        line_dict[line_index] = line
    case_dict[case_index] = line_dict

count = 0
for elem, val in case_dict.iteritems():
    count = count + 1
    #print "#####################################"
    #print val[0].split()
    ln1 = val[0].split()
    C = float(ln1[0])
    F = float(ln1[1])
    X = float(ln1[2])
    #print "C F X : ", C, F, X
    r = 2.0
    result =  "Case #" + str(count) + ": " + str(GetBestTime(r, C, F, X)) + "\n"
    g.write(result)
    
##
f.close()
g.close()
