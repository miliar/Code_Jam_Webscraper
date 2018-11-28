
def test(total,shylist):
    current=0
    added=0
    for shy in range(0,len(shylist)):
        addedthisround=0
        if current<shy:
            addedthisround=shy-current
            added+=addedthisround
        current+=shylist[shy]+addedthisround
    return added


f1=open("A-large.in")
l=f1.readline().strip()
total=int(l)

for i in range(0,total):
    l=f1.readline().strip()
    contents=l.split()
    total1=int(contents[0])
    shylist=[ord(ch)-ord('0') for ch in contents[1]]
    
    result=test(total1,shylist)
    print "Case #%d: %d"%(i+1,result)
    
