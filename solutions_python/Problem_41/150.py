#from __future__ import division
#from math import log

# code jam template
filein="1b2.in"
fileout="1b.out"


def rest(s,x):
    t=list(s)
    t.remove(x)
    return t

def perm(s):
    if s==[]:
        return [[]]
    else:
        return reduce(lambda x,y:x+y,map(lambda x:[[x]+p for p in perm(rest(s,x))],s))


def order(digits):
    return map(lambda x:int(''.join(map(str,x))),sorted(perm(digits)))

def solve(num):
    d=map(int,list(num))+[0]
    allofthem=sorted(set(order(d)))
    i=allofthem.index(int(num))
    return allofthem[i+1]


# load data
# paste basic example
datain="""
3
115
1051
6233
"""
#or
datain=open(filein).read()
dataout=open(fileout,"w")

# data as lines of data
data=[x for x in datain.split('\n') if x]

for i,row in enumerate(data[1:]):
    ans=solve(row)

    # "text" is the output string for one case
    text='Case #%d: %s'%(i+1,str(ans))
    dataout.write(text+'\n')
    print text
    

# close data file
dataout.close()
print "Wrote %s" % fileout

