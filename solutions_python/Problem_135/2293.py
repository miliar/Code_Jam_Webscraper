##
workdir = "C:\codejam2014\\"
input_file = "A-small-attempt0.in"
#print input_file.split(".")
output_file = input_file.split(".")[0] + ".out"
inp = workdir + input_file
outp = workdir + output_file
f = open(inp, 'rU')
g = open(outp, 'w')
T = int(f.readline())
case_size = 10
#print("#cases: ", T)
##
case_dict = {}
for case_index in range(T):
    line_dict = {}
    for line_index in range(case_size):
        line = f.readline()
        line_dict[line_index] = line
    case_dict[case_index] = line_dict

for elem, val in case_dict.iteritems():
    #print "###  Case# ", elem+1, "####"
    firstrowindex = int(val[0].split()[0])
    secondrowindex = int(val[5].split()[0])
    #print firstrowindex
    #print secondrowindex
    rowa = set(val[firstrowindex].split())
    rowb = set(val[secondrowindex+5].split())
    #print rowa
    #print rowb
    intersection_len =  len(rowa & rowb)
    if intersection_len == 0.0:
	    ln1 = "Case #"+str(elem+1)+": " + "Volunteer cheated!" + "\n"
	    print ln1
	    g.write(ln1)
    elif intersection_len > 1:
	    ln2 = "Case #"+str(elem+1)+": " + "Bad magician!" + "\n"
	    print ln2
	    g.write(ln2)
    else:
	    ln3 = "Case #"+str(elem+1)+": " + list(rowa & rowb)[0] + "\n"
	    print ln3
	    g.write(ln3)
##
f.close()
g.close()
