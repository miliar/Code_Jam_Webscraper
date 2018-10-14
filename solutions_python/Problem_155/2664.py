f = '/Users/pruth/Downloads/A-large.in'
# f = '/Users/pruth/Downloads/sample.txt'
l = []
out = open('/Users/pruth/Downloads/A-large-1.txt',"w")
with open(f) as txt:
    a = txt.readlines()
    for i,x in enumerate(a):
        a[i]=x.strip('\n')
        
def processCase(c,v,n,co):
    
    stoodUp = 0
    needInvite = 0
    # print v
    for i,x in enumerate(v):
        # print 'need ',i,'have',stoodUp
        x=int(x)
        
        if stoodUp >= i:
            stoodUp+=x
        else :
            # print "invited ",i-stoodUp
            needInvite += i-stoodUp
            stoodUp+=i-stoodUp
            stoodUp+=x
    if n==co:
        out.write("Case #%s: %s"%(n,needInvite))
    else:
        out.write("Case #%s: %s\n"%(n,needInvite))
    # print "Case #%s: %s"%(n,needInvite)
    # print '\n'


def process(count,lines):
    for i in xrange(count):
        c,v = lines[i].split(' ')
        c= int(c)
        processCase(c,v,i+1,count)
    
      
count = int(a[0])
lines = a[1:]
process(count,lines)

