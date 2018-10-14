d = {
	2: 1,
	3: 2,
	4: 3,
	5: 5,
	6: 8,
	7: 14,
	8: 24,
	9: 43,
	10: 77,
	11: 140,
	12: 256,
	13: 472,
	14: 874,
	15: 1628,
	16: 3045,
	17: 5719,
	18: 10780,
	19: 20388,
	20: 38674,
	21: 73562,
	22: 140268,
	23: 268066,
	24: 513350,
	25: 984911,
}

lines = open("C-small-attempt3.in").read().split("\n")

T = int(lines[0])

output = []
for i in xrange(1, T+1):
	n = int(lines[i])
	r = d[n] % 100003
	
	output.append("Case #"+str(i)+": "+ str(r))
	
print "\n".join(output)
open("result.out", "w").write("\n".join(output))
	