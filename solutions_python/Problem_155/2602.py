



def standing_novation(input):
	invited = 0
	standing = 0

	for x in xrange(len(input)):
		e = int(input[x])
		

		if standing < x:
			invited += (x - standing)
			standing += (x - standing)

		standing += e

	return invited





fin_path = "/Users/better/Downloads/A-large.in"

def fout_path(fin_path):
	k = fin_path.split("/")
	j = k[-1].split(".")
	if len(j) > 1:
		j[-2] += "_answer"
	else: j[-1] += "_answer"

	k[-1] = ".".join(j)

	return "/".join(k)


fin  = open(fin_path)
fout = open(fout_path(fin_path), "w")

print fout_path(fin_path)

line_count = 0
count = 1
for line in fin:
	line_count += 1
	if(line_count == 1): continue

	ret = standing_novation(line.split(" ")[-1].strip())
	print count , ret
	fout.writelines("Case #"+str(count)+": "+ str(ret)+"\n")
	count += 1

	fout.flush()


fout.close()




