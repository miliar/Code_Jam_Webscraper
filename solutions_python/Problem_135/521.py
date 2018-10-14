import sys,os

def findcard(row1,row2):
    # compare the two selected rows and find common cards
    cards = []
    for c in range(4):
        if row1[c] in row2:
            cards.append(row1[c])
            
    l = len(cards)
    if l == 0:
        return('Volunteer cheated!')
    if l == 1:
        return(cards[0])
    if l>1:
        return('Bad magician!')
    
    
def magictrick(infile,outfile):
    
    testcases = int(infile.readline())
    
    # for each testcase, read out the selected rows and compare with findcard()
    # then write the output line in outfile
    for t in range(testcases):
        i = int(infile.readline())
        for r in range(4):
            line = infile.readline()
            if r==i-1:
                row1 = line.replace('\n','').split(' ')
        j = int(infile.readline())
        for r in range(4):
            line = infile.readline()
            if r==j-1:
                row2 = line.replace('\n','').split(' ')

        answer = findcard(row1,row2)
        
        outfile.write('Case #'+str(t+1)+': '+answer+'\n')
        

def main(argv):
    
    # read input file from command line arguments
    # pass input and output files to program
    if len(argv)!=1:
        print('Inputfile missing!')
    else:
        try:
            infile = open(argv[0],'r') 
            (fname,extension) = os.path.splitext(argv[0])
            outfile = open(fname+'.out','w')
            magictrick(infile,outfile)
            infile.close()
            outfile.close()
        except IOError as e:
            print(e)


if __name__ == "__main__":
  main(sys.argv[1:])