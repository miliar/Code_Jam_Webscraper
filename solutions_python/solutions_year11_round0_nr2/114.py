def parse(s):
    ret=[]
    for i in xrange(2):
        l=int(s[0])+1
        ret.append(s[1:l])
        s=s[l:]
    ret.append(s[1])
    return ret

for case in range(input()):
    comb,opp,inv=parse(raw_input().split())
    #print comb,opp,inv
    elems=[]
    for e in inv:
        elems.append(e)
        #check comb
        changed=True
        while changed:
          changed=False
          for c in comb:
            if len(elems)>1 and (elems[-2]+elems[-1]==c[:2] or elems[-1]+elems[-2]==c[:2]):
                elems.pop()
                elems.pop()
                elems.append(c[2])
                changed=True
                break
        #check opp
        for o in opp:
            if o[0] in elems and o[1] in elems:
                elems=[]
                break
    print "Case #"+str(case+1)+":",
    print repr(elems).replace("'","")
