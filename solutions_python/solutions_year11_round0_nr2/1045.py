inputFile=open('cjb_input_sm.txt','r')
outputFile=open('cjb_output.txt','w')
cases=int(inputFile.readline())

for line in range(cases):
    input=inputFile.readline().strip('\n')
    input=input.split(' ')
    c=int(input[0])
    d=int(input[c+1])
    n=int(input[c+1+d+1])
    cdict={}
    combs=[]
    for x in range(1,c+1):
        cdict[input[x][0:2]]=input[x][2]
        combs+=[input[x][0:2]]
    ddict={}
    opps=[]
    for x in range(c+2, c+2+d):
        ddict[input[x][0]]=input[x][1]
        ddict[input[x][1]]=input[x][0]
        opps+=[input[x][0]]
        opps+=[input[x][1]]
    seq=input[len(input)-1]
    elist=[]
    for c in seq:
        elist+=[c]
        l=len(elist)
        if(l>1):
            if elist[l-2]+elist[l-1] in combs:
                elist=elist[:-2]+[cdict[elist[l-2]+elist[l-1]]]
            elif elist[l-1]+elist[l-2] in combs:
                elist=elist[:l-2]+[cdict[elist[l-1]+elist[l-2]]]
            elif elist[l-1] in opps:
                if ddict[elist[l-1]] in elist[:l-1]:
                    elist=[]

    outputFile.write('Case #' +str(line+1)+': [')
    for x in range(len(elist)):
        outputFile.write(elist[x])
        if x!=len(elist)-1:
            outputFile.write(', ')
    outputFile.write(']\n')

outputFile.close()
inputFile.close()
    
