def input():
    filename="B-small-attempt1.in"
    infile=open(filename,"r")
    num_cases=int(infile.readline())
    print num_cases,"cases"
    count=0
    cases=[]
    for line in infile:
        count+=1
        case=[]
        for i in line.split():
            case.append(int(i))
        cases.append(case)
        print "case#",count," ",str(case)
    infile.close()
    if count != num_cases:
        print "error in number of cases"
    return (num_cases,cases)



        
def process(case):
    print
    num_dancer=case[0]
    num_surprise=case[1]
    num_p=case[2]
    scores=case[3:]
    if len(scores) != num_dancer:
        print "num of scores dont match"
    print num_dancer,"dancers",num_surprise,"surprises",num_p,"is the score needed"
    print "scores are ",str(scores)
    normal=0
    surprise=0
    normal=0
    surprise=0
    result=0
    for score in scores:
        print "looking at ",score
        nfound=False
        sfound=False
        start=num_p-2
        end=10
        if(start<0):
            start=0
        if(end>10):
            end=10
        for x in range(start,end+1):
            if nfound:
                break
            for y in range(start,end+1):
                if nfound:
                    break
                for z in range(start,end+1):
                    if nfound:
                        break
                    if (x+y+z==score) and (x>=num_p or y>=num_p or z>=num_p) and (x<=10 and y<=10 and z<=10):
                            if not abs(x-y) >2:
                                if not abs(x-z) > 2:
                                    if not abs(z-y) > 2:
                                        if abs(x-y) <2 and abs(x-z)<2 and abs(y-z)<2:
                                            nfound=True
                                            print x,y,z,"possible"
                                        else:
                                            sfound=True
                                            print x,y,z,"surprise"
        if nfound==True:
            print score,"is possible"
            normal+=1
        elif sfound==True:
            print score,"is surprising"
            surprise+=1
        else:
            print score,"is not possible"

    print surprise,normal
    if  num_surprise <=surprise:
            return normal+num_surprise
    else:
            return normal+surprise
           

#main()
(num_cases,cases)=input()
outfilename="output.txt"
outfile=open(outfilename,"w")
count=0
for case in cases:
    print case
    result= process(case)
    count+=1
    outfile.write("Case #"+str(count)+": "+str(result)+"\n")
outfile.close()
