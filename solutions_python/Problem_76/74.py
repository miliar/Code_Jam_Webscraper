"""
Code Jam 2011 Qualification Round
CandySplitting by Warren Usui
"""
def CandySplitting(fileHead):
    rootd = 'C:\\wutemp\\CodeJam\\2011'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        fin.readline()
        txtin = fin.readline()
        charnums = txtin.split(" ")
        minv = int(charnums[0])
        xornumb = 0
        sumv = 0
        for numba in charnums:
            nval = int(numba)
            xornumb ^= nval
            sumv += nval
            if nval < minv:
                minv = nval
        outstr = "NO"
        if xornumb == 0:
            outstr = str(sumv-minv)
        odata = "Case #{0}: {1}\n".format(iterv+1, outstr)
        fout.write(odata)
        
if __name__ == '__main__':
    CandySplitting('C-large')
