




outfile=open('outfileA_SO2','w')

with open("A-large.in") as fil:
    cases=int(fil.readline())
    out=""
    for case in xrange(cases):
        testline=fil.readline().split()
        Smax=int(testline[0]); S=testline[1]
        nbr_aud=int(S[0])
        nbr_requ=0
        for i in xrange(1,len(S)):
            if(int(S[i])!=0):
                new_nbrequ=i-nbr_aud
                if nbr_aud<i and new_nbrequ>nbr_requ:
                    nbr_requ = new_nbrequ
                nbr_aud+=int(S[i])
        out+=str("Case #")+str(case+1)+str(": ")+str(nbr_requ)+str("\n")
        
    
print out
outfile.write(out)
outfile.close()
