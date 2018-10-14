
def printMove():
    sean=[]
    patrick=[]
    N = input()
    raw = raw_input()
    raw=raw.split(' ')
    for i in xrange(0,len(raw)):
        raw[i]=int(raw[i])
    raw.sort(reverse=True)
    #print raw

    #VALIDITY
    xor=0
    for i in xrange(0,len(raw)):
        xor = xor ^ raw[i]
    if xor is not 0:
        return "NO"
        #return
    s = 0
    for i in xrange(0,len(raw)-1):
        s = s + raw[i]
        
    return s



import sys
sys.stdin.close()
sys.stdin = open("3in.txt", "r")

sys.stdout = open("3out.txt", "w") 
T = input()
for i in xrange(0,T):
    print "Case #{0}: {1}".format(i+1,printMove())

sys.stdout.close()
