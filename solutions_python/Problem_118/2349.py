infile = open("C-small-attempt0.in", "rU")
outfile = open("C-small.out", "w")

linenum = 0
casenum = 1

nums = [1, 4, 9, 121, 484]

for line in infile:
    if linenum != 0:                
        endpoints = line.strip().split(" ")
        a = int(endpoints[0])
        b = int(endpoints[1])

        count = 0
        for n in nums:
            if a <= n and n <= b:
                count += 1

        outfile.write("Case #%d: %d\n" % (casenum, count))
        
        casenum += 1
        
    linenum += 1

outfile.close()
