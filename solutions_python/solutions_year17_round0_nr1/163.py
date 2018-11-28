IN_FILE = "A-large.in"

infile = open(IN_FILE)
out = open("A.out","w")

cases = int(infile.readline())

def flip(pancakes, k, i):
    for j in range(i,i+k):
        pancakes[j] = 1-pancakes[j]
    return pancakes

for case in range(cases):
    print "\n"
    print "Case #%i" %(case+1)
    out.write("Case #%i: " %(case+1))
    
    pancakes,k = infile.readline().split()
    k = int(k)
    vals = []
    for c in pancakes:
        vals.append(1 if c == "+" else 0)
    print vals
    
    cnt = 0
    for i in range(len(vals)-k+1):
        if vals[i] == 0:
            vals = flip(vals,k,i)
            cnt += 1
            #print vals
            
    if 0 in vals:
        out.write("IMPOSSIBLE\n")
        print "IMPOSSIBLE"
    else:
        out.write(str(cnt)+"\n")
        print cnt
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()
out.close()