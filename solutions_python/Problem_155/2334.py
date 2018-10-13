import sys

input = "A-large.in"
output = "A-large.out"
fin = open(input, "r");
fout = open(output, "w")

orig_stdout = sys.stdout
sys.stdout = fout

num = int(fin.readline())

for i in range(num):
	standpeople = 0
	highestneed = 0
	parts = fin.readline().split(" ")
	maxshy = int(parts[0])
	list = parts[1]
	for level in range(maxshy+1):
		need = level - standpeople
		highestneed = max(need, highestneed)
		standpeople += int(list[level])
	print "Case #" + str(i+1) + ": " + str(highestneed)

fin.close()
fout.close()
