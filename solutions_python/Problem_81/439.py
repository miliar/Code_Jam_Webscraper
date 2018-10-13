"""
Code Jam 2011 Round 1
problemA by Warren Usui
"""
def cwp(pattern):
    win = 0.
    loss = 0.
    for x in pattern:
        if x == '.':
            continue
        if x == '1':
            win += 1
        else:
            loss += 1
    return [win,loss]
    
def calcp(wl):
    total = wl[0] + wl[1]
    if total == 0:
        return 0.
    return wl[0]/total

def cowp(plist,indx):
    mypat = plist[indx]
    cnt = 0
    pct = 0.
    ocnt = 0.
    for i in xrange(0,len(plist)):
        x = mypat[i]
        if not x == '.':
            ocnt += 1
            patr = plist[cnt]
            orec = cwp(patr)
            if x == '1':
                orec[1] -= 1
            if x == '0':
                orec[0] -= 1
            pct += calcp(orec)
        cnt += 1
    if ocnt == 0:
        return 0.
    return pct/ocnt
            
def problemA(fileHead):
    rootd = 'C:\\Documents and Settings\\Owner\\My Documents\\Downloads'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        teamn = int(fin.readline())
        rec = []
        for _ in xrange(0,teamn):
            rec.append(fin.readline().strip())
        wp = []
        owp = []
        oowp = []
        for i in xrange(0,teamn):
            wp.append(calcp(cwp(rec[i])))
            owp.append(cowp(rec,i))
        for i in xrange(0,teamn):
            mypat = rec[i]
            cnt = 0
            ocnt = 0.
            otot = 0.
            for x in mypat:
                if not x == '.':
                    otot += owp[cnt]
                    ocnt += 1
                cnt += 1
            if ocnt == 0:
                oowp.append(0)
                continue
            oowp.append(otot/ocnt)
        odata = "Case #{0}:\n".format(iterv+1)
        fout.write(odata)
        for i in xrange(0,teamn):
            rpi = .25 * wp[i] + .5 * owp[i] + .25 * oowp[i]
            ostr = str(rpi)+'\n'
            fout.write(ostr)
        
if __name__ == '__main__':
    problemA('A-large')