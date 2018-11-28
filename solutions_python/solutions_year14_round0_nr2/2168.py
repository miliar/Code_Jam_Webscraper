infile = open("B-large.in")

def inp():
    return infile.readline()

outfile = open("jam2_large.out", mode = 'w')

def out(s):
    print(s, file=outfile)
    
for test in range(int(inp())):
    c, f, x = map(float, inp().split())
    t = float('inf')
    farm_time = 0
    n = 0
    while 1:
        tnew = x/(2+n*f) + farm_time
        if tnew > t:
            res = str(t)
            break
        else:
            t = tnew
            farm_time += c/(2+n*f)
            n += 1
    out("Case #" + str(test+1) + ": " + res)
        
infile.close()
outfile.close()
