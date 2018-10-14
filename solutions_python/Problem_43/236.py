import glob,os


for files in glob.glob("*.in"):
    if(os.path.exists(files.replace(".in",".out"))):
        continue

    fin = open(files)

    ans=[]
    T=int(fin.readline())
    for ttt in range(0, T):
        w=fin.readline().strip()
        l=len(w)
        cnt=[1,0]+[i for i in range(2,200)]
        vals={}
        vals2=[]
        tot=0
        bases=0
        for x in range(0,l):
            xv=w[x]
            if(not vals.has_key(xv)):
                vals[xv]=cnt.pop(0)
                bases+=1
            vals2.append(str(vals[xv]))
        if(bases<2):
            bases=2
        ans.append("Case #%d: %d"%(ttt+1,int("".join(vals2),bases)))

    fout=open(files.replace(".in",".out"), "w+")
    fout.write("\r\n".join(ans))
    fin.close()
    fout.close()
