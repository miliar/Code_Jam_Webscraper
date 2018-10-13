filename = "A-small-attempt1"
infile = open("{}.in".format(filename))
outfile = open("{}.out".format(filename), 'w')

trans = str.maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")

T = int(infile.readline())
for t in range(1,T+1):
    line = infile.readline().strip()
    outfile.write("Case #{}: {}\n".format(t, line.translate(trans)))

infile.close()
outfile.close()
