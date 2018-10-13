def todec(s,alp):
    b=len(alp)
    x=0
    j=0
    for i in reversed(s):
        n=alp.find(i)
        x+=n*b**j
        j+=1

    return x

T=int(raw_input())
for case_no in range(1,T+1):    
    s=raw_input()
    alp=[]
    for i in s:
        if i not in alp:
            alp.append(i)
    
    if len(alp)==1: alp.append(chr(255))
    alp.insert(1,alp.pop(0))    
    alp=''.join(alp)
    
    print "Case #%d: %d" % (case_no, todec(s,alp))
