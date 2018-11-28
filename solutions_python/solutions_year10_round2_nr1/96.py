import psyco
psyco.full()

def main():
    def mk(l):
        nl=[]
        for x in xrange(len(l)):
            if x==0:
                nl.append(l[x])
            else:
                nl.append(nl[x-1]+"/"+l[x])

        return nl
            
    def comb(l1,l2):
        for x in l1:
            if x in l2:
                continue
            else:
                l2.append(x)
        return l2
            
    def fix(r,gi,s):
#        print "r=",r, "gi=", gi, "s=",s
        list=r.split("/")
        list=mk(list)
 #       print mk(list)
        c=len(gi)
        gi=comb(list,gi)
        s+=len(gi)-c
        return gi, s
        
    
  
    cases = int(raw_input())
    for i in xrange(0, cases):
        N, M = map(int, raw_input().split(" "))
        given=[]
        req=[]
        sum=0
        for j in xrange(N):
            g = map(str, raw_input()[1:].split("/"))
            given=comb(mk(g),given)
 #       print given   
        for k in xrange(M):
            dir = raw_input()[1:]
            if dir in given:
                continue
            else:
                given, sum = fix(dir,given,sum)
  #      print given   
        print "Case #%i: %i" % (i+1, sum)
        
           
main()