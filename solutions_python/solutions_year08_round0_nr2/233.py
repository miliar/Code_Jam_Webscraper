#!/usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
#coding=utf-8

input = file("B-large.in", "r")
#input = file("input.txt", "r")
case = int(input.readline())
#print case
for c in range(case):
    s = {}
    r = int(input.readline())
#    print n
    t = input.readline().split(" ")
    na = int(t[0])
    nb = int(t[1])
    for i in range(na):
        t=input.readline().split(" ")
        if s.has_key(int(t[0][:2])*60+int(t[0][3:])):
            s[int(t[0][:2])*60+int(t[0][3:])].append((1,"a"))
        else:
            s[int(t[0][:2])*60+int(t[0][3:])] = [(1,"a")]
            
        if s.has_key(int(t[1][:2])*60+int(t[1][3:])+r):
            s[int(t[1][:2])*60+int(t[1][3:])+r].append((-1,"b"))
        else:
            s[int(t[1][:2])*60+int(t[1][3:])+r] = [(-1,"b")]
        
        #s.append((int(t[1][:2])*60+int(t[1][3:])+r,-1,"b"))
    for i in range(nb):
        t=input.readline().split(" ")
        if s.has_key(int(t[0][:2])*60+int(t[0][3:])):
            s[int(t[0][:2])*60+int(t[0][3:])].append((1,"b"))
        else:
            s[int(t[0][:2])*60+int(t[0][3:])] = [(1,"b")]
            
        if s.has_key(int(t[1][:2])*60+int(t[1][3:])+r):
            s[int(t[1][:2])*60+int(t[1][3:])+r].append((-1,"a"))
        else:
            s[int(t[1][:2])*60+int(t[1][3:])+r] = [(-1,"a")]
        
    #s.sort()
    ss = s.items()
    ss.sort()
    #print ss
    na = nb = 0
    mna = mnb = 0
    for (k,v) in ss:
#        print k,v
        da = 0
        db = 0
        for vs in v:
            if vs[1] == 'a':
                da += vs[0]
            if vs[1] == 'b':
                db += vs[0]
        na += da
        nb += db
        if mna < na:
            mna = na
        if mnb < nb:
            mnb = nb
            
        #print na,nb
    print "Case #"+str(c+1)+": "+str(mna)+" "+str(mnb)


    
