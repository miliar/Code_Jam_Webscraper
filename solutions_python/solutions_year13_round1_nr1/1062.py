import sys,math
 
def readline_ints():
    return [int(num) for num in fin.readline().strip().split()]

# <codecell>

# Update this with the filename
fname = "A-small-attempt5"
with open(fname+".in","r") as fin, open(fname+".out","w") as fout:

    numcases = readline_ints()[0]
    #print(numcases, "cases")
    
    for caseno in range(1, numcases+1):
        # Code goes here
        
        ran=readline_ints()
        
        r=ran[0]
        t=ran[1]

        result = .25*(1-2*r+math.sqrt(4*r**2-4*r+1+8*t))
        result = int(result)
        
        outstr = "Case #%d: %s" % (caseno, result)
        fout.write(outstr + "\n")
        #print r, t, outstr
