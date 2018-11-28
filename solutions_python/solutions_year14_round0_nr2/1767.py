infile = open('input.txt','r')
outfile = open('output.txt','w')
def buy(c,f,x,k):
    s = 2
    result = 0
    for i in range(k):
        result = result + c / (s+i*f)
    result = result + x / (s + k*f)
    return result
lines = infile.readlines()
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
n = int(lines[0])
for i in range(n):
    line = lines[i+1].split()
    s = 2
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    t = x/s
    m = 1
    t1 = buy(c,f,x,m) 
    while t1 < t:
        t = t1
        m = m + 1
        t1 = buy(c,f,x,m)
    print "Case #"+str(i+1)+": "+str(t)
    outfile.write("Case #"+str(i+1)+": "+str(t)+"\n")
