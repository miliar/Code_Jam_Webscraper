output = open("A-large.out", "w")
input =  open("A-large.in", "r")
tests = int(input.readline())
for i in range(1,tests+1):
	line=input.readline()
	NK=line.rsplit(" ")
	N=int(NK[0])
	K=int(NK[1])
	output.write("Case #")
	output.write(str(i))
	output.write(": ")
	if (K+1) % 2**N ==0:
		output.write("ON")
	else:
		output.write("OFF")
	output.write("\n")