import tkFileDialog
import sys

def gorosort(cost, positions, numbers, start):
    if start + 1 > len(numbers):
        print("%s - nothing to do" % numbers)
        print("%s - nothing to do" % positions)
        return cost
    if positions[start + 1] == start:
        print("%s - no cost" % numbers)
        print("%s - no cost" % positions)
        return gorosort(cost, positions, numbers, start + 1)
    else:
        toSwap = positions[start + 1]
        print "start: %d" % start
        print "toSwap: %d" % toSwap
        numbers[toSwap] = numbers[start]
        numbers[start] = start + 1
        positions[start + 1] = start
        positions[numbers[toSwap]] = toSwap
        print(numbers)
        print(positions)
        return gorosort(cost + 2, positions, numbers, start + 1)

def find_chains(start, numbers, chain, chains):
#    print "start: %s, chain: %s, chains: %s" % (start, chain, chains)
    if (start + 1 > len(numbers)):
        return chains
#    print numbers[start]
    if numbers[start] in chain:
        chains.append(chain)
        return find_chains(start + 1, numbers, [], chains)
    for ch in chains:
        if numbers[start] in ch:
            return find_chains(start + 1, numbers, [], chains)
    chain.append(numbers[start])
    return find_chains(numbers[start] - 1, numbers, chain, chains)

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
            positions = {}
            for position, number in enumerate(numbers):
                positions[number] = position
            print("%s - starting numbers" % numbers)
#            print("%s - starting positions" % positions)
            chains = find_chains(0, numbers, [], [])
            print("%s - chains" % find_chains(0, numbers, [], []))
            sum = 0
            for chain in chains:
                if len(chain) > 1:
                    sum += len(chain)
            output = "%0.6f" % sum 
#            cost = gorosort(0, positions, numbers, 0);
#            output = "%0.6f" % cost
            print "Output: %s" % output
            of.write("Case #%d: %s\n" % (caseNo, output))
            caseNo += 1
    of.close()
        
if __name__ == '__main__':
    sys.setrecursionlimit(3000)
    main()