"""
Code Jam 2011 Round 1
FreeCell by Warren Usui
"""
def getFrac(pct):
    a = pct
    if a == 0:
        return [0,1]
    bot = 100
    for div in [2,5]:
        while (a % div == 0) and (bot % div == 0):
            a /= div
            bot /= div
    return [a,bot]
def FreeCell(fileHead):
    rootd = 'C:\\Documents and Settings\\Owner\\My Documents\\Downloads'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    BROKE = "Broken"
    for iterv in xrange(0,number):
        txt = fin.readline()
        cnumbs = txt.split(" ")
        nval = int(cnumbs[0])
        pd = int(cnumbs[1])
        pg = int(cnumbs[2])
        fd = getFrac(pd)
        ans = BROKE
        if fd[1] <= nval:
            ans = "Possible"
            if (pg == 100) and (pd < 100):
                ans = BROKE
            if (pg == 0) and (pd > 0):
                ans = BROKE
        odata = "Case #{0}: {1}\n".format(iterv+1, ans)
        fout.write(odata)
        
if __name__ == '__main__':
    FreeCell('A-large')