import sys
sys.stdin=open("/home/kshitij/Downloads/A-small-attempt0.in","r")
sys.stdout=open("/home/kshitij/Downloads/output.out","w")
t=int(raw_input())
for c in range(t):
    a1=int(raw_input())
    c1=[]
    for i in range(4):
        c1.append(map(int,raw_input().split()))
    s1=set(c1[a1-1])
    a2=int(raw_input())
    c2=[]
    for i in range(4):
        c2.append(map(int,raw_input().split()))
    s2=set(c2[a2-1])
    res=list(s1.intersection(s2))
    #print s1,s2
    if len(res)>1:
        print "Case #%s: Bad magician!"%(c+1)
    elif len(res)==0:
        print "Case #%s: Volunteer cheated!"%(c+1)
    else:
        print "Case #%s: %s"%(c+1,res[0])
sys.stdout.close()
