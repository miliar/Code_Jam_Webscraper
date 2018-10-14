import sys
filename = "samp.txt"
if len(sys.argv) > 1:
    filename = sys.argv[-1]
    
data = [map(int,x.strip().split()) for x in open(filename,'r').readlines()[2::2]]

for (num,case) in enumerate(data):
    if(reduce(lambda x,y:x^y,case) <> 0):
        print "Case #%d: NO"%(num+1)
    else:
        print "Case #%d: %d"%(num+1,sum(case)-min(case))

