mapping={}
trainin="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv\n"
trainout="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up\n"
for i in range(0,len(trainin)):
	mapping[trainin[i]]=trainout[i]
mapping['z']='q'
mapping['q']='z'
print sorted(mapping.values())
len(mapping)

infilename="challenge1.in"
outfilename="challenge1.out"

infile = open(infilename)
outfile= open(outfilename,"w")

ncases=int(infile.readline())

for casenumber in range(1,ncases+1):
	line = infile.readline()
	s=""
	for char in range(0, len(line)):
		s+=mapping[line[char]]
	outfile.writelines("Case #"+str(casenumber)+": "+s)
