import sys,os

def honestwar(N,naomi,ken):
    nwins = 0
    for p in range(N):
        nchoice = naomi.pop()
        kchoice = [x for x in ken if x>nchoice]
        if len(kchoice)==0:
            ken.remove(min(ken))
            nwins+=1
        else:
            ken.remove(min(kchoice))
    return nwins
    
def deceitfulwar(N,naomi,ken):
        
    naomi.sort()
    ken.sort()
        
    compare = [ naomi[i]>ken[i] for i in range(len(naomi)) ]
    while False in compare:
        # naomi chooses the smallest element            
        nchoice = naomi.pop(0)
        ken.pop()
        compare = [ naomi[i]>ken[i] for i in range(len(naomi)) ]

    nwins = len(naomi)        
        
    return nwins
        
    
def war(infile,outfile):
    
    testcases = int(infile.readline())
    
    for t in range(testcases):
        N = int(infile.readline())
        n = [float(i) for i in infile.readline().replace('\n','').split(' ')]
        k = [float(i) for i in infile.readline().replace('\n','').split(' ')]
        
        answer1 = deceitfulwar(N,n[:],k[:])
        answer2 = honestwar(N,n[:],k[:])

        outfile.write('Case #'+str(t+1)+': '+str(answer1)+ ' ' +str(answer2)+'\n')


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
            war(infile,outfile)
            infile.close()
            outfile.close()
        except IOError as e:
            print(e)


if __name__ == "__main__":
  main(sys.argv[1:])