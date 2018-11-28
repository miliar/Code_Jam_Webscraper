T=int(input())
for t in xrange(T):
    seq = str(raw_input())
    seq = seq.split()
    x=0
    p=int(seq[0])
    pairs,des={},{}
    while( x<p):
        x+=1
        z=seq[x]
        pairs[(z[0],z[1])] = z[2]
        pairs[(z[1],z[0])] = z[2]
    p=int(seq[x+1])
    i=0
    while( i < p):
        i+=1
        z=seq[x+i+1]
        des[z[0]]=z[1]
        des[z[1]]=z[0]
    awe= []
    x= x+i
    z=seq[x+3]
    for x in z:
        if len(awe) == 0 :
            awe.append(x)
        else:
            if(  (awe[len(awe) -1 ], x) in pairs.keys()):
                cc=(awe[len(awe) -1 ], x)
                awe.pop()
                awe.append( pairs[cc])
            elif(x in des.keys()):
                if( des[x] in awe):
                    awe=[]
                else:
                    awe.append(x)
            else:
                awe.append(x)
    x= '[' + (', ').join(awe) + ']'
    print "Case #%d: %s"%(1+t,x)

    #print "DFDF",seq[x+3],seq
    #print pairs,des

