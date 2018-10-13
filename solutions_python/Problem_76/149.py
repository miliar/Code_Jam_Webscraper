import tkFileDialog
import sys

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
            noNumbers = int(line)
            print("Number of numbers: %d" % noNumbers)
            line = f.readline()
            numbers = [int(x) for x in line.split()]
            bitwiseExclusiveOrForAll = reduce(lambda x, y:x ^ y, numbers)
            if(bitwiseExclusiveOrForAll == 0):
                output = str(sum(sorted(numbers)[1:]))
            else:
                output = "NO"
            print "Output: %s" % output
            of.write("Case #%d: %s\n" % (caseNo, output))
            caseNo += 1
    of.close()
    
        
if __name__ == '__main__':
    main()