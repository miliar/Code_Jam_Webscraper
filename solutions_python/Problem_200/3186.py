
import pandas as pd
import numpy as np

def maxtidy(n,c):
    a=np.array(([int(e) for e in str(n)]))
    if len(a)>1:
        steps=(a[1:]-a[:-1])<0
        if not steps.any():
            return "Case #"+str(c)+": "+str(n)
        else:
            hely=np.where(steps)[0][0]
            ertek=a[hely]
        elso=np.where(a==ertek)[0][0]
        a[elso]=a[elso]-1
        a[(elso+1):]=9
        if a[0]==0:
            return "Case #"+str(c)+": "+"".join([str(e) for e in a[1:]])
        else:
            return "Case #"+str(c)+": "+"".join([str(e) for e in a])
    else:
        return "Case #"+str(c)+": "+str(n)

df=pd.read_csv("B-large.in",skiprows=1,sep=" ",header=None)
df["c"]=df.index.map(lambda x: x+1)

#df["solution"]=df.apply(lambda row: maxtidy(row[0],row["c"]),axis=1)
#df

f=open("B-small.out","w")
f.write("\n".join(df.apply(lambda row: maxtidy(row[0],row["c"]),axis=1).tolist()))
f.close()