import sys
import os.path

def main(argv):
    if (len(argv)==1):
        print("No argument!\n")
        return
    
    if(not os.path.isfile(argv[1])):
        print("input file does not exist!\n")
        return

    inname=argv[1]
    outname=argv[1][:-2]+'out'

    with open(inname,"r") as inputFile:
        num=int(inputFile.readline())
        for i in range(num):
            res=""
            line=inputFile.readline().rstrip('\n').split(' ')
            a=int(line[0])
            b=int(line[1])
            k=int(line[2])

            count=0
            for m in range(a):
                for n in range(b):
                    win=m&n
                    if (win<k):
                        count+=1

            res=str(count)
            with open(outname,"a") as out:
                out.write("Case #"+str(i+1)+": "+res+"\n")
        

if __name__=="__main__":
    main(sys.argv)
