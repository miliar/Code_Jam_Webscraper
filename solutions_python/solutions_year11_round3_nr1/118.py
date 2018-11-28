import tkFileDialog
import sys
import string

def transform(grid, R, C):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#':
                if (i == R - 1 or j == C - 1):
                    return True
                if (grid[i+1][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j+1] == '#'):
                    print "replacing for i, j: %s, %s" % (i,j)
                    
                    newrow1 = grid[i][:j] + '/\\'
                    newrow2 = grid[i+1][:j] + '\\/'
                    if (j + 1 < C):
                        newrow1 += grid[i][j+2:]
                        newrow2 += grid[i+1][j+2:]
                    print grid[i] + " replaced with " + newrow1
                    print grid[i+1] + " replaced with " + newrow2
                    grid[i] = newrow1
                    grid[i+1] = newrow2
                else:
                    return True
    return False

def main():
    infile = (len(sys.argv) > 1 and sys.argv[1]) or tkFileDialog.askopenfilename(title="Select input file", initialdir='.', filetypes = [('Input','.in')])
    outfile = infile.replace(".in", ".out", 1);
    print "Output file will be: %s" % outfile
    of = open(outfile, "w")
    with open(infile, "r") as f:
        line = f.readline()
        noCases = int(line)
        print "Number of test cases: %d" % noCases 
        caseNo = 1
        while caseNo <= noCases:
            line = f.readline()
            (R, C) = [int(x) for x in line.split()]
            print("R, C: %d, %d" % (R, C))
            grid = []
            for i in range(R):
                line = f.readline()
                grid.append(line.rstrip())
            impossible = transform(grid, R, C)
            if impossible:
                output = "Impossible\n"
            else:
                output = ""
                for i in range(R):
                    output += grid[i] + "\n"
                print "Output:\n%s" % output
            of.write("Case #%d:\n%s" % (caseNo, output))
            caseNo += 1
    of.close()
        
if __name__ == '__main__':
    main()