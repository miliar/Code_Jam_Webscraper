from string import maketrans
def main():

        sampleFilename = "A-small-attempt0.in"
        inFile = open(sampleFilename,"r")
        outFile = open("outputfile.txt","w")
        originalSet = "abcdefghijklmnopqrstuvwxyz"
        GooglereseSet ="ynficwlbkuomxsevzpdrjgthaq"
        mapSet = maketrans(GooglereseSet, originalSet)
        noOfT = int(inFile.readline().rstrip())
        for i in range (0,noOfT):
            line = inFile.readline().rstrip()
            line = line.translate(mapSet)
            OutputLine = "Case #{0:d}: ".format(i+1)
            OutputLine = OutputLine + line
            OutputLine = OutputLine + "\n"
            outFile.write(OutputLine);
main()
	
