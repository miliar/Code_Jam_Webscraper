#Python 2.6 on Windows XP
#Jonathan Hsu
#Google Codejam 2009

#Alien Language
#converts patterns to regex

import re
import glob
import os

for filename in glob.glob("*.in"):
    outfile=filename.replace(".in",".out")
    if(os.path.exists(outfile)):
        continue
    f=open(filename)

    l,d,n=[int(i) for i in f.readline().split()]
    dic=[f.readline() for i in range(d)]
    dic="".join(dic)

    pat=[re.compile("^"+f.readline().replace("(","[").replace(")","]").strip()+"$",re.MULTILINE) for i in range(n)]

    j=0
    ans=["Case #%d: %d"%(i+1,max([0,len(pat[i].split(dic))-1])) for i in range(n)]
    ff=open(outfile,"w+")
    ff.write("\n".join(ans))

    ff.flush()
    ff.close()
    f.flush()
    f.close()
