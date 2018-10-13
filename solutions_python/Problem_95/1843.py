#code jam 1a

input_file_name = "A-small-attempt2.in";
output_file_name = "cj1a_out.txt";
def translate(cypher):
	key =  "abcdefghijklmnopqrstuvwxyz ";
	code = "yhesocvxduiglbkrztnwjpfmaq ";
	translation = "";
	length = cypher.__len__();
	for i in range(length):
		translation+=code[key.index(cypher[i])];
	return translation;

input = [];

infile = open(input_file_name,"r");
while infile:
	line = infile.readline();
	if line:
		input.append(line.strip());
	else:
		break;


numcases = int(input[0]);

translations = [];
for i in range(numcases):
	j= i+1;
	output = "Case #"+str(j)+": "+translate(input[j]);
	print output;
	translations.append(output);
	

OUTFILE = open(output_file_name, "w");
OUTFILE.write("\n".join(translations));
OUTFILE.close();


