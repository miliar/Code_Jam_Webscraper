fl = open('A-large.in','r')
case=int(fl.readline())
sta=['Push','Stay','Move']
class O:
    pos=1
    stat=sta[1]
class B:
    pos=1
    stat=sta[1]

    
for j in range(case):
    z=(fl.readline().strip().split())[1:]
    for i,k in enumerate(z):
        try:z[i]=int(k)
        except:pass
    s=[[k,z[i+1]] for i,k in enumerate(z) if i%2==0 ]
    o=[]
    b=[]
    ocl=O()
    bcl=B()
    opath=[]
    bpath=[]
    for x,y in s:
        if x=='O':
            o.append(y)
        elif x=='B':
            b.append(y)
    for x in o:
        if ocl.pos==x:
            ocl.stat=sta[0]
            opath.append(ocl.stat)
        while ocl.pos!=x:
            if ocl.pos<x:
                ocl.pos+=1
                ocl.stat=sta[2]
                opath.append(ocl.stat)
            if ocl.pos>x:
                ocl.pos-=1
                ocl.stat=sta[2]
                opath.append(ocl.stat)
            if ocl.pos==x:
                ocl.stat=sta[0]
                opath.append(ocl.stat)
    for x in b:
        if bcl.pos==x:
            bcl.stat=sta[0]
            bpath.append(bcl.stat)
        while bcl.pos!=x:
            if bcl.pos<x:
                bcl.pos+=1
                bcl.stat=sta[2]
                bpath.append(bcl.stat)#+" "+str(bcl.pos)
            if bcl.pos>x:
                bcl.pos-=1
                bcl.stat=sta[2]
                bpath.append(bcl.stat)
            if bcl.pos==x:
                bcl.stat=sta[0]
                bpath.append(bcl.stat)
    '''
    op=(i for i in opath)
    bp=(i for i in bpath)
    for x,y in s:
        try:
            if x=='O':
                sexo=op.next()
                sexb=bp.next()
                if sexo==sta[0]:
                    if sexb==sta[0]:
                        finalpath.append([sexo,sta[1]])
                        sexo=op.next()
                    else:
                        finalpath.append([sexo,sexb])
                        sexo=op.next()
                        sexb=bp.next()
                else:
                    while sexo!=sta[0]:
                        if sexb!=sta[0]:
                            finalpath.append([sexo,sexb])
                            sexo=op.next()
                            sexb=bp.next()
                        elif sexb==sta[0]:
                            finalpath.append([sexo,sta[1]])
                            sexo=op.next()
                    
            if x=='B':

                while sexb!=sta[0]:
                    if sexo!=sta[0]:
                        sexo=op.next()
                        sexb=bp.next()
                        finalpath.append([sexo,sexb])
                    elif sexo==sta[0]:
                        sexb=bp.next()
                        finalpath.append([sta[1],sexb])
        except:pass
    '''
    c=1
    for h,l in s:
        if h=='O':
            for i,k in enumerate(opath):
                if k==sta[0]:
                    opath[i]=c
                    c+=1
                    break
        if h=='B':
            for i,k in enumerate(bpath):
                if k==sta[0]:
                    bpath[i]=c
                    c+=1
                    break
    '''
    try:
        ind=opath.index(1)+1
    except:
        ind=bpath.index(1)+1
    for i in range(1,len(s)):
        try:
            x=opath.index(i)
            x=opath.index(i+1)
            ind=ind+opath.index(i+1)-opath.index(i)-1
        except:pass
        try:
            x=bpath.index(i)
            x=bpath.index(i+1)
            ind=ind+bpath.index(i+1)-bpath.index(i)-1
        except:pass
        try:
            if (opath.index(i+1)+1)>ind:
                ind=opath.index(i+1)+1
            else:
                ind+=1
        except: pass
        try:
            if (bpath.index(i+1)+1)>ind:
                ind=bpath.index(i+1)+1
            else:
                ind+=1
        except: pass
    '''
    for i in range(len(s)):
        if opath.count(i+1)==1 and opath.count(i+2)==1:
            oi=opath.index(i+1)
            oi1=opath.index(i+2)
            continue
        if bpath.count(i+1)==1 and bpath.count(i+2)==1:
            oi=bpath.index(i+1)
            oi1=bpath.index(i+2)
            continue
        if opath.count(i+1)==1 and bpath.count(i+2)==1:
            oi=opath.index(i+1)
            oi1=bpath.index(i+2)
            if oi<oi1:
                continue
            else:
                while oi>=oi1:
                    bpath.insert(oi1,"*")
                    oi=opath.index(i+1)
                    oi1=bpath.index(i+2)
                continue
        if bpath.count(i+1)==1 and opath.count(i+2)==1:
            oi=bpath.index(i+1)
            oi1=opath.index(i+2)
            if oi<oi1:
                continue
            else:
                while oi>=oi1:
                    opath.insert(oi1,"*")
                    oi=bpath.index(i+1)
                    oi1=opath.index(i+2)
                continue
    if opath.count(len(s))==1:
        ind=len(opath)
    if bpath.count(len(s))==1:
        ind=len(bpath)
    print "Case #%d:"%(j+1),ind
