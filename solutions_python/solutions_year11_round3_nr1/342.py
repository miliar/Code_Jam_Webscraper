"""
Code Jam 2011 Round 1
problemA by Warren Usui
"""
def  checkRow(grid,row,col):
    tcnt = 0
    for i in xrange(0,row):
        for j in xrange(0,col):
            if grid[i][j] == '#':
                tcnt += 1
            else:
                if tcnt % 2 == 1:
                    return False
                tcnt = 0
        if tcnt % 2 == 1:
            return False
        tcnt = 0
    return True
def  checkCol(grid,row,col):
    tcnt = 0
    for i in xrange(0,col):
        for j in xrange(0,row):
            if grid[j][i] == '#':
                tcnt += 1
            else:
                if tcnt % 2 == 1:
                    return False
                tcnt = 0
        if tcnt % 2 == 1:
            return False
        tcnt = 0
    return True
     
def problemA(fileHead):
    rootd = 'C:\\Documents and Settings\\Owner\\My Documents\\Downloads'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        rcv = fin.readline().split(' ')
        row = int(rcv[0])
        col = int(rcv[1])
        grid = []
        for _ in xrange(0,row):
            grid.append(fin.readline())
        impval = False
        if checkRow(grid,row,col):
            if checkCol(grid,row,col):
                impval = True
        odata = "Case #{0}:\n".format(iterv+1)
        fout.write(odata)
        if not impval:
            fout.write("Impossible\n")
        else:
            ogrid = []
            for i in xrange(0,row):
                lyne = []
                for j in xrange(0,col):
                    lyne.append(grid[i][j])
                ogrid.append(lyne)
            for i in xrange(0,row):
                for j in xrange(0,col):
                    if ogrid[i][j] == '#':
                        ogrid[i][j] = '/'
                        ogrid[i+1][j+1] = '/'
                        ogrid[i+1][j] = '\\'
                        ogrid[i][j+1] = '\\'
            for i in xrange(0,row):
                ostr = ''
                for j in xrange(0,col):
                    ostr += ogrid[i][j]
                ostr += '\n'
                fout.write(ostr)
if __name__ == '__main__':
    problemA('A-large')