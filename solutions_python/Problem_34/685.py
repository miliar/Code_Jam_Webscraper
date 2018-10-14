inp=open('file2.txt')
out=open('output1.txt','w') 
info=inp.readline()
infolist=info.split()
wl=eval(infolist[0])
wc=eval(infolist[1])
test=eval(infolist[2])
words=[]
for i in range(0,wc):
    words.append(inp.readline())
for t in range(0,test):
    line=inp.readline()
    main=[]
    k=0
    while k<=wl:
        tm=line[0]
        if tm=='\n':
            break
        if tm!='(' and tm!=')':
            main.append(tm)
            line=line[1:]
            k+=1
            if k==wl:
                break
        else:
            index=line.find(')')
            main.append(line[1:index])
            k+=1
            if k==wl:
                break
            line=line[index+1:]
    total=0    
    for s in words:
        i=0
        while main[i].find(s[i])!=-1:
            i+=1
            if i>wl-1:
                total+=1
                break
    #print 'Case #%d: %d'%(t+1,total)
    out.write('Case #%d: %d\n'%(t+1,total))
inp.close()
out.close()

