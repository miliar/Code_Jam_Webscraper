infile = open("DATA.txt")
infile = infile.readlines()
for i, v in enumerate(infile):
    infile[i] = v.strip()
i = open("DATA.txt", "w")
for ii in infile:
    if ii != "":
        i.write(ii+"\n")
print infile