#from __future__ import division
#from math import log

# code jam template
filein="1Alarge.in"
fileout="1Alarge.out"

def parse(tree):
    ans=tree.replace('(',' ( ').replace(')',' ) ')
    tree=[x for x in ans.split(' ') if x]
    return tree

def process(tree,names,p):
    tree=tree[1:-1]
    if len(tree)==1:
        return p*float(tree[0])
    else:
        count=0
        for i,x in enumerate(tree[2:]):
            if x=='(':
                count+=1
            elif x==')':
                count-=1
            if count==0:
                if tree[1] in names:
                    return process(tree[2:2+i+1],names,p*float(tree[0]))
                else:
                    return process(tree[2+i+1:],names,p*float(tree[0]))

def solveone(tree,test):
    tests=[x for x in test.split(' ') if x]
    name=tests[0]
    n=tests[1]
    names=tests[2:]
    return process(tree,names,1)

##def solve(tree,tests):
##    for test in tests:
##        solveone(tree,test)
            

# load data
# paste basic example
datain="""
2
3
(0.5 cool
  ( 1.000)
  (0.5 ))
2
anteater 1 cool
cockroach 0
13
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
3
beaver 2 furry freshwater
trout 4 fast freshwater fishy rainbowy
dodo 1 extinct
"""
#or
datain=open(filein).read()
dataout=open(fileout,"w")

# data as lines of data
data=[x for x in datain.split('\n') if x]


cases=int(data[0])
atrow=1
for c in range(cases):
    text='Case #%d:'%(c+1)
    print text
    dataout.write(text+'\n')

    num=int(data[atrow])
    tree=''.join(data[atrow+1:atrow+num+1])
    tree=parse(tree)
    atrow+=num+1
    numtest=int(data[atrow])
    for test in data[atrow+1:atrow+numtest+1]:
        text='%0.7f'%solveone(tree,test)
#        print text
        dataout.write(text+'\n')
    atrow+=numtest+1
    

# close data file
dataout.close()
print "Wrote %s" % fileout

