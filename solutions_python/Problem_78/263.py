def writeResult(fout, lnum, result):
    out.write('Case #%d: ' % (lnum))
    if(result):
        out.write('Possible\n')
    else:
        out.write('Broken\n')


f = open('A-small-attempt0.in','r')
out = open('smalloutput.txt','w')

numlines = int(f.readline())

fracResults = {}

for i in range(numlines):
    vals = f.readline().split(' ')
    
    n = int(vals[0])
    pd = int(vals[1])
    pg = int(vals[2])
    
    if(pg == 0 and pd != 0):
        writeResult(out, i+1, False)
        continue
    
    if(pd == 100):
        writeResult(out, i+1, True)
        continue
    
    if(pg == 100 and pd < 100):
        writeResult(out, i+1, False)
        continue
        
    if(pd == 0 and pg < 100):
        writeResult(out, i+1, True)
        continue
    
    done = False
    for denom in range(1,n+1):
        for numer in range(1,denom):
            
            fval = float(numer) / float(denom)
            #print numer, '\t', denom, '\t', fval
            if(fval * 100 == pd):
                done = True
                break
        if(done):
            break
    if(done):
        writeResult(out, i+1, True)
    else:
        writeResult(out, i+1, False)
    
        
f.close()
out.close()
        