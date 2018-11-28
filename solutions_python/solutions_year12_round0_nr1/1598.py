import string;

fin = open("A-small.in", "r");
fout = open("A-small.out", "w");

caseNum = fin.readline();

dict = {'y':"a", 'n':"b", 'f':"c", 'i':"d", 'c':"e", 'w':"f",'l':"g", 'b':"h", 'k':"i", 'u':"j", 'o':"k", 'm':"l", 'x':"m", 's':"n", 'e':"o",'v':"p", 'z':"q", 'p':"r", 'd':"s", 'r':"t", "j":"u", "g":"v", "t":"w", "h":"x", "a":"y", "q":"z"};

for case in range(int(caseNum)):
    pw = fin.readline();
    s = str();
    for char in pw:
	if char == " ":
	    s = s + char;
        elif char in string.ascii_lowercase:
            s = s + dict[char];
    fout.write("Case #" + str(case + 1) +": " + s + "\n");

fin.close();
fout.close();
