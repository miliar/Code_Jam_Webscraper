inp = open('../in.txt')
outp = open('../out.txt', 'w')

cases = int(inp.readline())
for cs in range(cases):
    line = inp.readline().split()
    r = (int)(line[0])
    t = (int)(line[1])
    rings = 0
    while t > 0:
        t -= 2*r+1
        r += 2
        if(t >= 0):
            rings += 1
    outp.write('Case #'+str(cs+1)+': '+str(rings)+'\n')      

inp.close()
outp.close()