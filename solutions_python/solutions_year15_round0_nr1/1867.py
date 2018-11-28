testfile=open('A-large.in','r')
text=testfile.readlines()
ndata=[]
for i in range(1,len(text)):
    ndata.append(text[i].replace('\n',''))
    ndata[i-1]=ndata[i-1].split()
    del ndata[i-1][0]
    ndata[i-1]=ndata[i-1][0]
for k in range(len(ndata)):
    tp=0
    tot=0
    for j in range(len(ndata[k])):
        if j>tot:
            tp=tp+(j-tot)
            tot=tot+(j-tot)
        tot=tot+int(ndata[k][j])
    print "Case #{}:".format(k+1),tp
testfile.close()       
    
