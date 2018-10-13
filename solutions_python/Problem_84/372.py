import glob
for file in glob.glob("A*.in"):
    fp=open(file)
    T=int(fp.readline())
    res=[]
    for i in range(T):
        R,C=map(int,fp.readline().strip().split())
        tiles=[]
        impos=0
        for j in range(R):
            tiles.append(list(fp.readline().strip()))
        for x in range(C):
            for y in range(R):
                if(tiles[y][x]=='#'):
                    if(y+1<R and x+1<C and tiles[y+1][x+1]=='#' and tiles[y+1][x]=='#' and tiles[y][x+1]=='#'):
                        tiles[y][x]=tiles[y+1][x+1]='/'
                        tiles[y+1][x]=tiles[y][x+1]='\\'
                    else:
                        impos=1
                        break
            if(impos==1):
                break
        if(impos==1):
            tiles=["Impossible"]
        else:
            tiles=["".join(x) for x in tiles]
        res.append("Case #%d:\n%s"%(i+1,"\n".join(tiles)))
    fp.close()
    fp=open(file+".out","w+")
    fp.write("\n".join(res))
    fp.close()
    