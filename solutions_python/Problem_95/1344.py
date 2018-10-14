from string import maketrans
infile = open("A-small-attempt0.in")
outfile = open("A-small-attempt0.out", "w")

lines = infile.readlines()
intab = " ynficwlbkuomxsevzpdrjgthaq "
outab = " abcdefghijklmnopqrstuvwxyz "
trantab = maketrans(intab, outab)

for i, line in enumerate(lines[1:]):
    outfile.write("Case #{}: ".format(i+1) + line.translate(trantab))

outfile.close()

