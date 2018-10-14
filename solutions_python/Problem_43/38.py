
def wf(fileName,ls):
    f = open(fileName,'w')
    for i,l in enumerate(ls):
        f.write('Case #%d: %s\n'%(i+1,l))

def minNum(ls):
    lsMap = []
    for x in ls:
        if x not in lsMap:
            lsMap.append(x)
    #print lsMap
    base = len(lsMap)
    d = {}
    d[lsMap[0]] = 1
    if base<=1:
        base = 2
    else:
        d[lsMap[1]] = 0
    cur = 2
    for i in lsMap[2:]:
        d[i] = cur
        cur += 1
    
    min = 0
    lsNew = []
    for i in ls:
        #lsNew.append[ d[i] ]
        min = min*base + d[i]
    
    return min

filename = 'Sample.in'
filename = 'A-small-attempt0.in'
filename = 'A-large.in'
f = open(filename)
contents = f.readlines()
s =contents[0].strip()
n = int(s)
print n
lsResult = []
for i in range(1,len(contents)):
    print i,'\t:',contents[i]
    nums = contents[i].strip()
    lsResult.append( minNum(nums) )
    

#print lsResult

    
wf(filename.split('.')[0]+'.out',lsResult)
