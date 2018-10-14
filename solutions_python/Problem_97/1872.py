inp = open('C-small-attempt1.in')
outp = open('out.txt','w')
cases = int(inp.readline())
x = 1
while x <= cases:

    line = inp.readline()
    line = line.split();
    A = int(line[0])
    B = int(line[1])
    recycled = 0

    n = A
    while n < B:
        m = n+1
        while m <= B:

            cut = 1
            while cut < len(str(n)):
                new = str(n)[cut:] + str(n)[:cut]
                if new == str(m):
                    recycled += 1
                    break
                cut += 1

            m += 1
        n += 1
            

    outp.write ("Case #"+str(x)+": "+str(recycled)+'\n')
    x += 1;
    
    
inp.close()
outp.close()
