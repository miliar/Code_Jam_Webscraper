#nbCases
#NGoog Surpr atLeastPAuMax TotalPourChaqGoogler

debug=0
#fname="numbers.txt"
fname="B-large.in"
file=open(fname)


out=open("out_"+fname, "w")


from pprint import pprint

    
nbCases=int(file.readline())
for k in range(1,nbCases+1):

    out.write("Case #"+str(k)+": ")


    line=file.readline()
    
    line=line.split()
    
    nbLin=int(line[0])
    nbCol=int(line[1])
    
    mat=[]
    
    for i in range(0, nbLin):
        line=file.readline()
        line=line.split()
        mat.append(line)
        
        
    
    pprint(mat)
    
    
    checAll=True
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            
            checA=True
            checB=True
            
            
            for a in range(0, len(mat)):
                
                if(int(mat[a][j])>int(mat[i][j])):
                    checA=False
                    
                    
            for b in range(0, len(mat[0])):
                
                if(int(mat[i][b])>int(mat[i][j])):
                    checB=False
            
            if (checA or checB)==False:
                checAll=False
                
    if checAll:
        out.write("YES\n")
    
    else:
    
        out.write("NO\n")
    
                
    #line=line[1:]
    #line=map(int,line)
    #from pprint import pprint
    #pprint(line)
    
    
    
    #test(line,k)
    
out.close()

#def m(l):
