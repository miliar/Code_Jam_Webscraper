infile = open("B-large.in", 'rb')
outfile = open("B-large.out", 'w')
lines = [x.lstrip().rstrip() for x in infile.readlines()]
probs = int(lines[0])

def simulate(c,f,x):
    
    t = 0.0
    curr = 0.0
    rate = 2.0

    while(True):
        o1 = x/rate
        o2 = c/rate + x/(rate+f)
        if (o1 < o2):
            t+=o1
            return t
        else:
            t+=c/rate
            rate += f

for p in range(1, probs+1):
    outfile.write("Case #"+str(p)+": ")
    C,F,X = [float(x) for x in lines[p].split()]
    outfile.write(str(round(simulate(C,F,X),7)))
    outfile.write("\n")
    
outfile.close()
