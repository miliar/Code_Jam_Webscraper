import sys

sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\B-large.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())
b = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']

for i in range(t):
    m = {}
    w = {}
    l = raw_input().split()
    j = 0
    c = int(l[j])
    j+=1
    while j<c+1 :
        m[(l[j][0],l[j][1])]=l[j][2]
        m[(l[j][1],l[j][0])]=l[j][2]
        j+=1
    d = int(l[j])
    j+=1
    while j<d+c+2:
        w[(l[j][0],l[j][1])] = 1
        w[(l[j][1],l[j][0])] = 1
        j+=1
    n = int(l[j])
    s = l[j+1]
    
    bb = []
    v = []
    v.append( s[0] )
    k=1
    if v[0] in b:
        bb.append(v[0])
    p = 0
    while k<n :
        if (s[k],v[p]) in m.keys():#check for combination
            #print 'combining',s[k],v[p] 
            v[p] = m[(s[k],v[p])]
            bb.pop()
        else:#check for deletion
            g = 0
            for e in bb:
                if (e,s[k]) in w.keys():
                    #print bb
                    #print 'clearing due to pair',e,s[k]
                    v = []
                    bb = []
                    p = 0
                    k+=1
                    if k<n :
                        v.append( s[k] )
                        bb.append(v[0])
                        #print 'appending1',v[0]
                    g=1
                    break
            if g == 0:
                #print 'appending2',s[k]
                bb.append(s[k])
                v.append(s[k])
                p+=1
        k+=1

    sys.stdout.write( "Case #"+str(i+1)+": [", )
    for x in range(len(v)-1):
        sys.stdout.write( v[x]+', ')
    if len(v)>0:
        sys.stdout.write( v[len(v)-1] )
    print ']'
    
    
        
        
