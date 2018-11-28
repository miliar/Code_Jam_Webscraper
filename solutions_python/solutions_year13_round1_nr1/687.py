
def codejam(infile,outfile):
    output=[]
    with open(infile,'r') as f:
        for z in range(int(f.readline())):
            line = f.readline().split()
            n,m = int(line[0]),int(line[1])
            outline = 'Case #'+str(z+1)+': '+str(solve(n,m))
            output.append(outline)

    with open(outfile,'w') as f:
        f.write('\n'.join(output))

def solve(r,t):
    y=-1
    while t>=0:
        y+=1
        t-=(2*r+1)
        r+=2
    return y
    
codejam("A-small-attempt0.in","A-small.out")
