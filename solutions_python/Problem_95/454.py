import string

in_file = open("A-small.in","r");
out_file = open("A-small.out","w");

case_num = 0;

# mappings determined from sample:
# for translating back from Googlerese
mapping = dict();
sample_in_file = open("sample.in","r");
sample_out_file = open("sample.out","r");
# sample files contain the example from the problem, formatted for easy processing

char_dict = {}
char_dict_out = {}

for line in sample_in_file:
    out_line = sample_out_file.readline()
    for x in xrange(0,len(line)):
        char_dict[line[x]] = out_line[x]
        
char_dict['q'] = 'z' #given to us
print len(char_dict)
print char_dict

googlerese = "abcdefghijklmnopqrstuvwxyz"
alphabet = ""
for i in googlerese:
    if i in char_dict:
        alphabet += char_dict[i]
    else:
        print "MIssing case: "+i 
        alphabet += "q" #specific case, sample+problem has every letter but q translated

# ? -> z
trans_table = string.maketrans(googlerese, alphabet)
casenum = 0;

for line in in_file:
    if (casenum == 0):
        casenum += 1
        continue
    newline = line.translate(trans_table)
    print newline
    out_file.write("Case #"+str(casenum)+": "+newline)
    casenum += 1

out_file.close()
