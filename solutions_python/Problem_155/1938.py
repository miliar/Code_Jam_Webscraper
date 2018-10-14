f=open("input.in", "r")
input=f.read().split()
f.close()
f=open("output.txt.", "w")
i=2
while i<len(input):
    standing=0
    invited=0
    levels=input[i]
    for j in range(len(levels)):
        if standing < int(j):
            invited+=j-standing
            standing=j
        standing+=int(levels[j])
    output="Case #{0}: {1}\n".format(str(i//2),str(invited))
    f.write(output)
    i+=2
f.close()
        

