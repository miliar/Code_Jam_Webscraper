d = {}
count = 0

f = open("first.txt","r")
g = open("firstout.txt","w")

index = 0

nums = f.readline().split()
l = int(nums[0])
lines = int(nums[1])
cases = int(nums[2])

m = list()
for x in xrange(26):
    d[chr(x+97)] = dict()

def traverse(lis,i,myd):
    global count
    if i == len(lis):
        count += 1
        #print "hi"
        return
    for x in xrange(len(lis[i])):
        #print lis[i][x]
        if lis[i][x] in myd:
            traverse(lis,i+1,myd[lis[i][x]])


for x in xrange(lines):
    s = f.readline().strip()

    myd = d[s[0]]
    for i in xrange(l-1):
        if i == l-2:
            myd[s[i+1]] = 1
            break
        if s[i+1] not in myd:
            myd[s[i+1]] = dict()
        myd = myd[s[i+1]]
        
#print d

for x in xrange(cases):
    s = f.readline().strip()
    i = 0
    lis = []
    while i < len(s):
        j = 0
        if s[i] == "(":
            while s[i+j] != ")":
                j += 1
            lis.append(s[i+1:i+j])
            i += j
        else:
            lis.append(s[i])
        i += 1
    count = 0
    traverse(lis,0,d)

    #print count
    
    g.write("Case #" + str(x+1) + ": " + str(count) + "\n")

f.close()
g.close()
