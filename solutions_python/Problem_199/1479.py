f1 = open("A-large.in","r").readlines()
f2 = open("results1.txt","w")
imp=False;
l1 = f1[0]
s = int(l1.split()[0])
cont=0
changedict = {'+':'-','-':'+'}
for i in range(s):
    line = f1[i+1].split()
    k = int(line[1])
    seq = list(line[0])
    leng = len(seq)
    for j in range(leng):
        if (seq[j]=='-'):
            if j+k-1>=leng:
                f2.write("Case #"+str(i+1)+": IMPOSSIBLE\n")
                imp=True
                break
            else:
                cont+=1
                for h in range(k):
                    seq[j+h]=changedict[seq[j+h]]
    if imp==False:
        f2.write("Case #"+str(i+1)+": "+str(cont)+"\n")
    else:
        imp=False
    cont=0
f2.close()
