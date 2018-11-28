inp = open("input.txt")
cases = int(inp.readline())
for case in range(cases):
    P, K, L = map(int, inp.readline().strip().split())
    ints = map(int, inp.readline().split())
    ints.sort(reverse=True)
    mult = 1
    total = 0
    while ints:
	total += sum(ints[:K])*mult
	del ints[:K]
	mult += 1
    print "Case #" + str(case+1) + ": " + str(total)

	
	