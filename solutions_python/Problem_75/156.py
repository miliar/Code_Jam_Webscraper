import tkFileDialog
import sys

def main():
    infile = (len(sys.argv) > 1 and sys.argv[1]) or tkFileDialog.askopenfilename(title="Select input file", initialdir='.', filetypes = [('Input','.in')])
    outfile = infile.replace(".in", ".out", 1);
    print "Output file will be: %s" % outfile
    with open(infile, "r") as f:
        lines = f.readlines()
    of = open(outfile, "w")
    print "Number of test cases: %d" % int(lines[0])
    for (caseNo, line) in enumerate(lines[1:]):
        tokens = iter(line.split())
        noCombs = int(tokens.next())
        combs = {}
        for i in range(noCombs):
            comb = tokens.next()
            combs[comb[0] + comb[1]] = comb[2]
            combs[comb[1] + comb[0]] = comb[2]
        dests = []
        noDests = int(tokens.next())
        for i in range(noDests):
            dest = tokens.next()
            dests.append(dest[0] + dest[1])
            dests.append(dest[1] + dest[0])
        print "Combinations: %s" % combs
        print "Destructions: %s" % dests
        sequenceLength = int(tokens.next())
        sequence = tokens.next()
        print "Sequence: %s" % sequence
        output = []
        for i in range(sequenceLength):
            print "Character: %s" % sequence[i]
            destFound = False
            if len(output) > 0:
                possibleComb = output[-1] + sequence[i]
                if possibleComb in combs:
                    print "comb found: %s" % possibleComb
                    output[-1] = combs[possibleComb]
                    formattedOutput = "[%s]" % ', '.join(output)
                    print "Output: %s" % formattedOutput
                    continue
                for j in range(len(output)):
                    possibleDest = output[j] + sequence[i]
                    if possibleDest in dests:
                        print "dest found: %s" % possibleDest
                        output = []
                        destFound = True
                        break
            if not destFound:
                output +=sequence[i]
            print "Output at %d: %s" % (i, output)
        formattedOutput = "[%s]" % ', '.join(output)
        print "Output: %s" % formattedOutput
        of.write("Case #%d: %s\n" % (caseNo + 1, formattedOutput))
    of.close()
        
if __name__ == '__main__':
    main()