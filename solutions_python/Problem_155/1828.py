
#lines = list(open("input.txt"))
lines = list(open("A-large.in"))
print(lines)
outFile = open("outputL.txt", "w")

for test in range(1, int(lines.pop(0))+1):
    
    vals = [int(x) for x in lines.pop(0).split()[1]]
    print(test, vals)
    
    extra = 0
    total = 0
    for i in range(0, len(vals)):
        print(i, total, vals[i])
        if total < i:
            extra += i-total
            total = i
        total += vals[i]

    print("final ", extra, total)
    outFile.write("Case #{}: {}\n".format(test, extra))
    
outFile.close()

