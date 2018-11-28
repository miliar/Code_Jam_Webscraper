
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %d\n'%(i+1,l))

hasMin = False
minB = 0
def bribe(num,ls,lsEmpty, numB):
    global hasMin
    global minB
    #print 'if ',num,ls,lsEmpty,numB
    for i,l in enumerate(ls):
        pre = 0
        post = num+1
        for x in lsEmpty:
            if x>pre and x<l:
                pre = x
            if x<post and x>l:
                post = x
        
        lsNew = ls[:]
        lsNew.remove(l)
        
        minThis = (l-pre-1)+(post-l-1)+numB
        
        if len(lsNew)==0:
            if hasMin:
                if minB>minThis:
                    minB = minThis
                    #print lsEmpty
            else:
                minB = minThis
                hasMin = True
        else:
            lsEmpty_New = lsEmpty[:]
            lsEmpty_New.append(l)
            lsT = ls[:]
            lsT.remove(l)
            bribe(num, lsT, lsEmpty_New, minThis)

filename = 'Sample.in'
filename = 'C-small-attempt0.in'
#filename = 'A-large.in'
f = open(filename)
contents = f.readlines()
print contents
s =contents[0].strip()
n = int(s)
print n
lsResult = []
for i in range(n):
    print i,'\t:',contents[2*i+1],contents[2*i+1+1]
    total = int(contents[2*i+1].strip().split()[0])
    ls = contents[2*i+1+1].strip().split()
    ls = [int(l.strip()) for l in ls ]
    hasMin = False
    bribe( total, ls, [], 0)
    lsResult.append( minB )
    
#print lsResult

    
wf(filename.split('.')[0]+'.out',lsResult)
