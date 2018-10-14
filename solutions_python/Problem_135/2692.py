
def Parseinput(s):
    returnlist=[0,0,0,0]
    for ii in range(4):
        if ii==3:
            returnlist[ii]=int(s)
        else:
            w=s.find(' ')
            returnlist[ii]=int(s[0:w])
            s=s[w+1:]
    return returnlist        

def matrixinput(r,inp):
    for j in range(4):
        r[j]=Parseinput(inp.readline())


def main():
    inputfile=open("A-small-attempt3.in","r+")
    num_test=int(inputfile.readline())
    outputfile=open("f0.txt","wb")
    row=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    row2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for t in range(num_test):
        accu=0
        num=0
        line=int(inputfile.readline())-1
        matrixinput(row,inputfile)
        line2=int(inputfile.readline())-1
        matrixinput(row2,inputfile)
        for i in row[line]:
            for j in row2[line2]:
                if i==j and accu==0:
                    num=i
                    accu+=1
                elif i==j:
                    accu +=1
        if accu==1:
            outputfile.write("Case #"+`t+1`+": "+`num`+"\n")
        elif accu>1:
            outputfile.write("Case #"+`t+1`+": Bad magician!"+"\n")
        else :
            outputfile.write("Case #"+`t+1`+": Volunteer cheated!"+"\n")
        if t==0:
            print accu
            
    outputfile.close()        
    
if __name__=="__main__":
    main()