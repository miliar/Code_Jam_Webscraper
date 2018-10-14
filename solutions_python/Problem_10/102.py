import sys

def func(x,y):
	x = int(x)
	y = int(y)
	return x.__cmp__(y)
    
def run():
    (length,keys,alpa) = lines.pop().split(" ")
    length = int(length)
    keys = int(keys)
    alpa = int(alpa)
    times = lines.pop().split(" ")
    times.sort(cmp=func)
    print times
    times.reverse()
    count = 1
    sum = 0
#    print "---------"
    for i in xrange(len(times)):
        count = ((i)/keys)+1
 #       print str(i)+" "+str(int(times[i]))+" "+str(count)
        sum += count*int(times[i])
    
    return sum


f = open(sys.argv[1])
suffix = ""
if (len(sys.argv) > 2):
    suffix = sys.argv[2]
lines = f.readlines()
f.close()
f = open(sys.argv[1]+".result_"+suffix+".txt","w")
lines.reverse()
times = int(lines.pop())
for k in xrange(times):
    f.write("Case #"+str(k+1)+": "+str(run())+"\n")
f.close()

