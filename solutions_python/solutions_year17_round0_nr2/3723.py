def tidy(n):
    if len(n) == 1:
        return n


    while True:    
        flag = False
        ilength = len(n)
        
        for i in range(1,len(n)):
            if int(n[i-1]) > int(n[i]):
                n = list(str(int(''.join(n))-1))
                flag = True
            if len(n) < ilength:
                return n

        if not flag:
            return n


infile = open("B-small-attempt1.in", "r")
outfile = open("B-small.out", "w")

t = infile.readline()
print(t)
casenumber = 1
for line in infile:
    n = list(line[:-1])
    n = tidy(n)
    n = ''.join(n)

    print("Case #{}: {}".format(casenumber, n), file=outfile)
    casenumber+=1

print("done")
infile.close()
outfile.close()
    
    
